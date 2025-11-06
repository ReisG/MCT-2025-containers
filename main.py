#! ./venv/bin/fastapi dev
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping_pong():
    return "pong"

@app.get('/visits')
def print_visits():
    return 2