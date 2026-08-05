words = input().split(",")
for word in words:
    print(f"self._{word} = {word}")

for word in words:
    print("@property\n"
          f"def {word}(self):\n"
          f"    return self._{word}\n")


manager = ProductsManager()
products = manager.get_products()  # pobiera wszystkie produkty
for product in products:
    print(product.name, product.price)  # dostęp do pól obiektu


import sqlite3
from contextlib import contextmanager

class ProductsManager:
    def __init__(self, database="data/"):
        self._products = []
        self.database = database

    @property
    def products(self):
        return self._products.copy()

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.database)
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def get_products(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")

            cursor.execute("SELECT * FROM products_table")
            self._products = cursor.fetchall()
            return self._products

    def return_products(self):
        return [prod for prod in self._products]

    def get_unique(self, category):
        tabUniques = sorted(list(set(self._products[category] for i in self._products)))
        tabUniques.insert(0, "Pokaż wszystkie")
        return tabUniques

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
        bd.execute_sql('data/db/create.sql', conn)
        bd.execute_sql('data/db/insert.sql', conn)
        bd.execute_sql('data/db/views.sql', conn)
    conn.close()
    return

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