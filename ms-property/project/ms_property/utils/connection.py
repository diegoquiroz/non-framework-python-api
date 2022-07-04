import os

from mysql.connector import connect, Error
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('/app/.env')
load_dotenv(dotenv_path)

DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_USER=os.getenv('DB_USER')
DB_PASS=os.getenv('DB_PASS')
DB_NAME=os.getenv('DB_NAME')

db_config = {
        'host': DB_HOST,
        'user': DB_USER,
        'password': DB_PASS,
        'database': DB_NAME,
        'port': DB_PORT
        }
connection = connect(**db_config)
