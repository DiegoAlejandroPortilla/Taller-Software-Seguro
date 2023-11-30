import psycopg2
import os

try:
    connection = psycopg2.connect(
        host="172.30.0.2",
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_DATABASE"),
        port=os.environ.get("DB_PORT")
    )
    print("Database connected successfully")
except Exception as ex:
    print("Error:", ex)