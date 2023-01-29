
# Hay que revisar por completo el fichero !!


from fastapi import FastAPI, Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET_KEY = '0aaea08713fb587a5397042592c77caf564a2d019419b8e3da871a20a0419bd0'
# Para obtener secrets keys se puede usar el comando: openssl rand -hex 32

# Para comprobar los JWT online: https://jwt.io

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "serbel": {
        "username": "serbel",
        "full_name": "Sergio Bellido",
        "email": "serbel@serbel.com",
        "disabled": False,
        "password": "$2y$12$a4WPg4b2No9.FDk35/hn1epSBhxGv29sVbyAVq09Eijv.T9um7rOK" # 123456
    },
    "admin": {
        "username": "admin",
        "full_name": "Administrador",
        "email": "admin@serbel.com",
        "disabled": True,
        "password": "$2y$12$ATtvuq1KUKzGzn6hHylGTu.E/wllpVP2Udsbb106gmzMZSvf7FR06" # admin
    },
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El nombre no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    
    access_token = {"sub":user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET_KEY , algorithm=ALGORITHM), "token_type": "bearer"}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación no válidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    try:
        username = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception


async def current_user(user: User = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación no válidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )
    return user


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user