from fastapi import FastAPI
from config import settings


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
