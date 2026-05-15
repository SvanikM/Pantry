import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def get_db():
    userDB = mysql.connector.connect(
      host=DB_HOST,
      user=DB_USER,
      password=DB_PASSWORD,
      database=DB_NAME
    )
    return userDB
#print(userDB)
#cursor = userDB.cursor()
#cursor.execute("SELECT * FROM users")
#print(cursor.fetchall())
#cursor.execute("SELECT * FROM ingredients")
#print(cursor.fetchall())
#cursor.close()
#userDB.close()


