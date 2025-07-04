import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

import urllib.parse as urlparse
url = urlparse.urlparse(DATABASE_URL)

db_name = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

try:
    conn = psycopg2.connect(
        dbname='postgres',
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE {db_name};")
    print(f"Database '{db_name}' created successfully!")

except psycopg2.errors.DuplicateDatabase:
    print(f"Database '{db_name}' already exists.")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals(): conn.close()
