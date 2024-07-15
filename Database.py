import sqlalchemy as sqlal
from dotenv import load_dotenv
import os
load_dotenv(".env")

connection = os.getenv("DB_CONNECTION_STRING")

engine = sqlal.create_engine(connection, connect_args={'connect_timeout': 60})


def Add_Account(data):
    with engine.connect() as conn:
        query = sqlal.text("INSERT INTO applications (job_id, full_name,email,resume_url) VALUES (:job_id, :full_name,:email,:resume_url)")

        conn.execute(query,{"job_id":job_id,"full_name":data.get("full_name"),"email":data.get("Email"),"resume_url":data.get("Resume")})
        conn.commit()