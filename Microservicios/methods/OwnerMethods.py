from config.db import connection

def create_id_owner ():
    cur = connection.cursor()
    cur.execute('SELECT MAX(ownerid) FROM owner')
    result = cur.fetchone()
    
    if result[0] is None:  # Si el resultado es vacío
        return 'ow01'
    
    
    letras = ""
    numeros = ""
    id = ""
    for i in result[0]:
        if i.isalpha():
            letras += i
        else:
            numeros += i
    print(numeros[0])
    if numeros[0]=="0":
        cambio  = int(numeros)+1
        nuevo = str(cambio)
        nuevo = "0"+nuevo
        id = letras+nuevo
        return id
    else:
        cambio = int(numeros)+1
        nuevo = str(cambio)
        id = letras+nuevo
        return id
    
def create_id_address():
    cur = connection.cursor()
    cur.execute('SELECT MAX(addressid) FROM address')
    result = cur.fetchone()

    if result[0] is None:  # Si el resultado es vacío
        return 'add01'
    
    letras = ""
    numeros = ""
    id = ""
    for i in result[0]:
        if i.isalpha():
            letras += i
        else:
            numeros += i
    if numeros[0] == "0":
        cambio = int(numeros) + 1
        nuevo = str(cambio)
        nuevo = "0" + nuevo
        id = letras + nuevo
        return id
    else:
        cambio = int(numeros) + 1
        nuevo = str(cambio)
        id = letras + nuevo
        return id
    
def create_id_parkingland():
    cur = connection.cursor()
    cur.execute('SELECT MAX(plid) FROM parkingland')
    result = cur.fetchone()

    if result[0] is None:  # Si el resultado es vacío
        return 'pl01'
    
    letras = ""
    numeros = ""
    id = ""
    for i in result[0]:
        if i.isalpha():
            letras += i
        else:
            numeros += i
    if numeros[0] == "0":
        cambio = int(numeros) + 1
        nuevo = str(cambio)
        nuevo = "0" + nuevo
        id = letras + nuevo
        return id
    else:
        cambio = int(numeros) + 1
        nuevo = str(cambio)
        id = letras + nuevo
        return id
    
def create_id_plot():
    cur = connection.cursor()
    cur.execute('SELECT MAX(plotid) FROM parkinglot')
    result = cur.fetchone()

    if result[0] is None:  # Si el resultado es vacío
        return 'po01'
    
    letras = ""
    numeros = ""
    id = ""
    for i in result[0]:
        if i.isalpha():
            letras += i
        else:
            numeros += i
    if numeros[0] == "0":
        cambio = int(numeros) + 1
        nuevo = str(cambio)
        nuevo = "0" + nuevo
        id = letras + nuevo
        return id
    else:
        cambio = int(numeros) + 1
        nuevo = str(cambio)
        id = letras + nuevo
        return id
    
def validate_username(str):
    cur = connection.cursor()
    cur.execute('SELECT ownerusername FROM owner')
    result = cur.fetchall()
    for i in result:
        if i[0] == str:
            return False
    return True

def validate_address(str):
    cur = connection.cursor()
    cur.execute('SELECT addressid FROM address')
    result = cur.fetchall()
    for i in result:
        if i[0] == str:
            return False
    return True

def validate_parkingland(str):
    cur = connection.cursor()
    cur.execute('SELECT plid FROM parkingland')
    result = cur.fetchall()
    for i in result:
        if i[0] == str:
            return False
    return True

def validate_parkinglot(str):
    cur = connection.cursor()
    try:
        connection.rollback()  # Realizar rollback para limpiar la transacción
        cur.execute('SELECT plotid FROM parkinglot')
        result = cur.fetchall()
        for i in result:
            if i[0] == str:
                return False
        return True
    except Exception as e:
        # Manejar el error aquí
        return False
    finally:
        cur.close()
