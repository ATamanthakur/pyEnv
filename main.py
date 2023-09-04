from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random

app = FastAPI()

@app.get("/")
def index():
    return {"message": "api server running"}

@app.get("/listing")
def generate_random_numbers():
    random_numbers = [random.randint(1,50) for _ in range(5)]
    return random_numbers

@app.get("/listing2")
def raise_505_err():
    raise HTTPException(status_code=505, detail="error 505")

@app.get("/listing3")
def raise_401_err():
    raise HTTPException(status_code=401, detail="error 401")

@app.get("/listing4")
def redirect_to_google():
    return RedirectResponse(url="https://www.google.com")