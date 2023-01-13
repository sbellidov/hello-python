from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

# Iniciar el servidor con: 'uvicorn main:app --reload'
# URL local en: http://127.0.0.1:8000

# Documentación (Swagger): http://127.0.0.1:8000/docs
# Documentación (Redocly): http://127.0.0.1:8000/redoc

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

# Statics files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def root():
    return {"url_curso": "https://mouredev.com/python"}

@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id": item_id}