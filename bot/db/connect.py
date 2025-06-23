import psycopg2 
import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")

def with_connection(f):
    def with_connection_(*args, **kwargs):
        conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASS, port=DB_PORT)
        cur = conn.cursor()
        result = f(cur, *args, **kwargs)
        conn.commit()
        conn.close()
        return result
    return with_connection_