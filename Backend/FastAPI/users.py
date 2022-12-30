from fastapi import FastAPI
# Iniciar el servidor con: uvicorn users:app --reload
from pydantic import BaseModel

app = FastAPI()

# Entidad users
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1, name="Sergio",surname="Bellido",age=38),
            User(id=2, name="Sofia",surname="Bellido",age=9),
            User(id=3, name="Alberto",surname="Bellido",age=6)
            ]

# Devuelve la lista completa de usuarios
@app.get("/usersclass")
async def usersclass():
    return users_list

# Devuelve el usuario según su 'id' indicado en el path
@app.get("/userid/{id}")
async def userid(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error: no se ha encontrado el usuario"}



# Esta forma es desaconsejada, poco eficiente
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Sergio", "surname":"Bellido", "age": 38},
            {"name":"Sofia", "surname":"Bellido", "age": 9},
            {"name":"Alberto", "surname":"Bellido", "age": 6}
            ]