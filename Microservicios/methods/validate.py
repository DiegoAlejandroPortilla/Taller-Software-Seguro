from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

# Clave secreta para firmar los tokens (debería ser segura y guardada de manera segura)
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Verifica aquí cualquier otra información del token que necesites
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o vencido",
        )
