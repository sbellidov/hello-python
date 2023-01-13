from fastapi import APIRouter, HTTPException
# Iniciar el servidor con: uvicorn users:app --reload
from pydantic import BaseModel

router = APIRouter()

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

# GET ------------------------- Lee

# Devuelve la lista completa de usuarios
@router.get("/users")
async def usersclass():
    return users_list

# ** PATH ** Devuelve el usuario según su 'id' indicado en el path
@router.get("/userid/{id}")
async def userid(id: int):
    return search_user(id)

# ** QUERY ** Consulta de un usuario desde query
@router.get("/userquery/") # Añadir ==> .../?id=1
async def user(id: int):
    return search_user(id)

# POST ------------------------- Inserta

@router.post("/user" , status_code = 201 )
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code = 404 , detail = "El usuario ya existe")
        # return {"El usuario ya existe"}
    users_list.append(user)
    return {"Usuario insertado con éxito !"}

# PUT ------------------------- Modifica

@router.put("/user")
async def user(user: User):
    found = False
    for index,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error: No se ha actualizado el usuario"}
    return {"Usuario modificado"}


# DELETE ------------------------- Borra

@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index,saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error: No se ha encontrado el usuario para eliminar"}
    return {"Usuario borrado"}


def search_user(id:int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error: no se ha encontrado el usuario"}


#---------------------------------------------
# Esta forma es desaconsejada, poco eficiente
@router.get("/usersjson")
async def usersjson():
    return [{"name":"Sergio", "surname":"Bellido", "age": 38},
            {"name":"Sofia", "surname":"Bellido", "age": 9},
            {"name":"Alberto", "surname":"Bellido", "age": 6}
            ]
#---------------------------------------------

