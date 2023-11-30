from fastapi import APIRouter,HTTPException,Depends
import config.db as db
from schemas.Owner import Owner  # Asumiendo que solo se necesita Owner
import methods.OwnerMethods as OwnerMethods
from methods.validate import verify_token  # Importa solo la función que necesitas
from cryptography.fernet import Fernet  # Para usar encriptación simétrica

APIOwner = APIRouter()

# Generar clave para el cifrado
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_data(data, cur):
    encrypted_data = []
    for row in data:
        encrypted_row = []
        for value in row:
            if isinstance(value, str):
                encrypted_value = fernet.encrypt(value.encode())
                encrypted_row.append(encrypted_value.decode())  # Convertir a texto para retornar
            else:
                encrypted_row.append(value)
        encrypted_data.append(tuple(encrypted_row))  # Convertir a tupla para evitar diccionarios
    return encrypted_data

@APIOwner.get('/owner')
async def list_owner():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM owner')
    result = cur.fetchall()

    encrypted_result = encrypt_data(result, cur)
    return encrypted_result


@APIOwner.get('/ownerdesc')
def list_owner_desc(token: str = Depends(verify_token)):
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM owner')
    result = cur.fetchall()

    columns = [desc[0] for desc in cur.description]  # Obtener los nombres de las columnas
    formatted_result = []
    for row in result:
        row_dict = dict(zip(columns, row))  # Convertir la tupla en un diccionario
        formatted_result.append(row_dict)

    return formatted_result


@APIOwner.post('/ownerdesc')
def create_owner(owner: Owner):
    new_owner = {
        "ownername": owner.ownername,
        "ownerlastname": owner.ownerlastname,
        "ownerusername": owner.ownerusername,
        "ownerpassword": owner.ownerpassword,
        "owneremail": owner.owneremail,
    }
    if OwnerMethods.validate_username(owner.ownerusername) == True:
        new_owner["ownerid"] = OwnerMethods.create_id_owner()
        cur = db.connection.cursor()
        cur.execute('INSERT INTO owner (ownerid, ownername, ownerlastname, ownerusername, ownerpassword, owneremail) VALUES (%(ownerid)s, %(ownername)s, %(ownerlastname)s, %(ownerusername)s, %(ownerpassword)s, %(owneremail)s)', new_owner)
        db.connection.commit()
        return "Owner created successfully"
    else:
        return "Username already exists"
    

from fastapi import HTTPException

@APIOwner.put('/owner/{owner_id}')
def update_owner(owner_id: str, owner: Owner, token: str = Depends(verify_token)):
    updated_owner = {
        "ownername": owner.ownername,
        "ownerlastname": owner.ownerlastname,
        "ownerusername": owner.ownerusername,
        "ownerpassword": owner.ownerpassword,
        "owneremail": owner.owneremail,
    }
    
    cur = db.connection.cursor()
    cur.execute('SELECT ownerid FROM owner WHERE ownerid = %s', (owner_id,))
    existing_owner = cur.fetchone()
    
    if existing_owner:
        cur.execute('''
    UPDATE owner
    SET 
        ownername = %(ownername)s,
        ownerlastname = %(ownerlastname)s,
        ownerusername = %(ownerusername)s,
        ownerpassword = %(ownerpassword)s,
        owneremail = %(owneremail)s
    WHERE ownerid = %(owner_id)s
''', {"owner_id": owner_id, **updated_owner})
        db.connection.commit()
        return "Owner updated successfully"
    else:
        raise HTTPException(status_code=404, detail="Owner not found")




@APIOwner.delete('/owner/{owner_id}')
def delete_owner(owner_id: str, token: str = Depends(verify_token)):
    cur = db.connection.cursor()
    cur.execute('SELECT ownerid FROM owner WHERE ownerid = %s', (owner_id,))
    existing_owner = cur.fetchone()
    
    if existing_owner:
        cur.execute('DELETE FROM owner WHERE ownerid = %s', (owner_id,))
        db.connection.commit()
        return "Owner deleted successfully"
    else:
        raise HTTPException(status_code=404, detail="Owner not found")

    
@APIOwner.get('/owner/{ownerusername}')
def validate_owner_user(ownerusername: str):
    cur = db.connection.cursor()
    cur.execute('SELECT ownerusername, ownerpassword FROM owner WHERE ownerusername = %s', (ownerusername,))
    result = cur.fetchall()
    return result  



