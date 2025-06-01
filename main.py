from fastapi import FastAPI
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()  # Load .env

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "MF Classifier is Live!"}

@app.get("/players")
def get_all_players():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM your_table_name"))
        return [dict(row) for row in result]