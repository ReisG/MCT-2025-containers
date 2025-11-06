#! ./venv/bin/fastapi dev
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import Request

from sqlmodel import Field, Session, SQLModel, create_engine

import config

db_url = "mysql://{DBUSER}:{DBPASSWORD}@{DBADDR}:{DBPORT}"
engine = None

class Ping(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ip: str

app = FastAPI()

@app.on_event("startup")
def on_startup():
    #connect to db
    global engine
    engine = create_engine(db_url, echo=True)

@app.get("/ping")
def ping_pong(request : Request):
    ip = request.client.host
    session = Session(engine)

    ping = Ping(ip=ip)
    session.add(ping)
    session.commit()

    session.close()
    return "pong"

@app.get('/visits')
def print_visits():
    return 2