
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/alfabeta")
def get_alfabeta():
    return {"Alfabeta": "Alfabeta"}

uvicorn.run(app, host="0.0.0.0", port=8001)