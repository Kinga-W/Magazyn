import sqlite3

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


def execute_sql(filename, engine):
    with open(filename, 'r', encoding='utf-8') as sql_file:
        sql_text = sql_file.read()

    with engine.connect() as connection:
        try:
            # Dla wielu instrukcji SQL w jednym pliku
            for statement in sql_text.split(';'):
                if statement.strip():
                    connection.execute(text(statement))
            connection.commit()
        except SQLAlchemyError as e:
            print(f"Błąd: {e}")
            connection.rollback()
