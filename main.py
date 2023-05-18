from typing import Union
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from sqlalchemy import text
import os 
from dotenv import load_dotenv

load_dotenv()

HOSTNAME = os.getenv("HOSTNAME")
PORT = os.getenv("PORT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DBNAME = os.getenv("DBNAME")    

MYSQL_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=MYSQL_URL)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/worker')
async def select_worker():
    query = db.session.query(text('SELECT * FROM test'))
    return query.all()