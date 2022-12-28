from fastapi import FastAPI

# Documentación en: http://127.0.0.1:8000/docs
# También en: http://127.0.0.1:8000/redoc

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def root():
    return {"url_curso": "https://mouredev.com/python"}

@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id": item_id}