import sqlite3
import os

current_dir = os.path.dirname(__file__)
db_name = os.path.join(current_dir, "database.db")


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, codigo INTEGER, nombre TEXT, precio REAL, stock INTEGER)")
        self.conn.commit()

    def insert_product(self, codigo, nombre, precio, stock):
        self.cur.execute("INSERT INTO productos VALUES (NULL, ?, ?, ?, ?)",
                         (codigo, nombre, precio, stock))
        self.conn.commit()

    def clear_products(self):
        # Elimina todos los registros de la tabla 'productos'
        self.cur.execute("DELETE FROM productos")
        self.conn.commit()

    def get_all_products(self):
        self.cur.execute("SELECT * FROM productos")
        products = self.cur.fetchall()
        return products

    def delete_product(self, product_code):
        self.cur.execute(
            "DELETE FROM productos WHERE codigo = ?", (product_code,))
        self.conn.commit()
