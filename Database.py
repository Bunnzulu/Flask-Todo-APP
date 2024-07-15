import sqlalchemy as sqlal
from dotenv import load_dotenv
import os
load_dotenv(".env")

connection = os.getenv("DB_CONNECTION_STRING")

engine = sqlal.create_engine(connection, connect_args={'connect_timeout': 60})

def Add_Account(data):
    file = open("UserNames.txt","r")
    words = file.read()
    UserNames = words.split("\n")
    file.close()   
    if data.get("Username") not in UserNames:
        with engine.connect() as conn:
            query = sqlal.text("INSERT INTO Accounts (username, password) VALUES (:username, :password)")
            conn.execute(query,{"username":data.get("Username"),"password":data.get("Password")})
            conn.commit()
        return True
    else:return False

def Get_Accounts():
    with engine.connect() as conn:
        result = conn.execute(sqlal.text("select * from Accounts"))
        Accounts = []
        for row in result.all():
            Accounts.append(dict(row._mapping))
        return Accounts

def Verify_Cred(data):
    for account in Get_Accounts():
        if account["username"] == data.get("Username") and account["password"] == data.get("Password"):
            return True
    return False
