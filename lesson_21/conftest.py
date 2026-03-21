import os

import psycopg2
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def conn():
    # Спроба підключитись до бази даних
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Connected to the database successfully!")

    except (Exception, psycopg2.Error) as error:
       pytest.fail("Error while connecting to PostgreSQL", error)

    yield connection
    connection.close()
    print("PostgreSQL connection is closed")


@pytest.fixture(scope="function")
def cursor_con(conn):
    # Для виконання запитів ви можете створити курсор
    cursor = conn.cursor()
    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД
    cursor.execute("SELECT version();")
    # Отримання результатів запиту
    record = cursor.fetchone()
    print("You are connected to - ", record)
    yield cursor , conn # conn.commit()
    conn.rollback()
    cursor.close()