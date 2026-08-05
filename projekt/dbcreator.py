import sqlite3

def execute_sql(filename, connection):

    with open(filename, 'r', encoding='utf-8') as sql_file:
        sql_text = sql_file.read()

    cursor = connection.cursor()
    try:
        cursor.executescript(sql_text)
        connection.commit()
    except Exception as e:
        print(f"Błąd: {e}")
        connection.rollback()

def main():
    conn = sqlite3.connect('data/db/warehouse.db')
    cursor = conn.cursor()

    cursor.execute("""
            SELECT count(*) FROM sqlite_master 
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
        """)
    table_count = cursor.fetchone()[0]
    if table_count == 0:
        print("Baza danych jest pusta, wczytuje baze.")
        execute_sql('data/db/create.sql', conn)
        execute_sql('data/db/insert.sql', conn)
        #execute_sql('data/db/views.sql', conn)
    conn.close()
    return

main()