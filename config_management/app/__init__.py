# app/__init__.py

from fastapi import FastAPI

app = FastAPI()

# Example route
@app.get("/")
async def read_root():
    return {"Hello": "World"}
