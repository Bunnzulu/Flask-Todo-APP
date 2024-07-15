import sqlalchemy as sqlal
from dotenv import load_dotenv
import os
load_dotenv(".env")

connection = os.getenv("DB_CONNECTION_STRING")

engine = sqlal.create_engine(connection, connect_args={'connect_timeout': 60})


def Add_Account(data):
    with engine.connect() as conn:
        query = sqlal.text("INSERT INTO Accounts (username, password) VALUES (:username, :password)")
        conn.execute(query,{"username":data.get("Username"),"password":data.get("Password")})
        conn.commit()