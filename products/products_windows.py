from tkinter import *
from products.database import Database
from tkinter import messagebox as alert
from tkinter import Toplevel
from tkinter import Menu
from tkinter import ttk
import tkinter as tk
import re


class ProductsWindow:
    def __init__(self, root):
        self.root = root
        self.products = []
        self.products_window = Toplevel(self.root)
        self.products_window.title('Productos')
        self.windows_styles(self.products_window, '1000x600')
        self.create_widgets()

        self.load_products_from_database()

        self.products_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        database = Database()
        database.clear_products()  # Limpiar todos los productos en la base de datos
        for product in self.products:
            # Insertar productos restantes
            database.insert_product(
                product[0], product[1], product[2], product[3])
        self.products_window.destroy()

    def load_products_from_database(self):
        # Cargar productos desde la base de datos
        self.clear_products_list()
        database = Database()
        products_from_db = database.get_all_products()
        for product in products_from_db:
            self.products.append(product)
            self.product_box.insert("", "end", values=product)

    def windows_styles(self, window, geometry: str):
        window.geometry(geometry)
        window.configure(bg='#333')
        frame = tk.Frame(window, bg='#333')
        frame.pack(expand=True, fill='both')

    def clear_products_list(self):
        self.products = []
        for item in self.product_box.get_children():
            self.product_box.delete(item)

    def delete_product(self):
        selected_item = self.product_box.selection()

        try:
            if selected_item:
                item_values = self.product_box.item(selected_item)['values']
                self.product_box.delete(selected_item)
                database = Database()

                product_code = item_values[0]
                database.delete_product(product_code)

                self.products = [
                    product for product in self.products if product[0] != product_code]
            else:
                alert.showerror(
                    'Error', 'Por favor selecciona un producto para eliminar')
        except:
            pass

    def create_widgets(self):
        self.create_treeview()
        self.create_delete_button()
        self.create_entry_fields_save_button()

    def create_treeview(self):

        self.product_box = ttk.Treeview(self.products_window, columns=(
            'Codigo', "Nombre", "Precio", "Stock"), show='headings')
        self.product_box.heading("Codigo", text="Codigo", anchor=CENTER)
        self.product_box.heading("Nombre", text="Nombre", anchor=CENTER)
        self.product_box.heading("Precio", text="Precio", anchor=CENTER)
        self.product_box.heading("Stock", text="Stock", anchor=CENTER)
        self.product_box.column("Codigo", anchor="center")
        self.product_box.column("Nombre", anchor="center")
        self.product_box.column("Precio", anchor="center")
        self.product_box.column("Stock", anchor="center")
        self.product_box.pack()

    def create_delete_button(self):
        button_delete = tk.Button(
            self.products_window, text='Eliminar', command=self.delete_product)
        button_delete.pack()

    def create_entry_fields_save_button(self):
        self.create_entry_fields()
        self.create_save_button()

    def create_entry_fields(self):
        self.data_code = IntVar()
        self.data_name = StringVar()
        self.data_price = IntVar()
        self.data_stock = IntVar()

        self.create_code_entry()
        self.create_price_entry()
        self.create_name_entry()
        self.create_stock_entry()

    def create_code_entry(self):
        label_code = tk.Label(self.products_window, text="Codigo:")
        label_code.pack()
        self.entry_code = tk.Entry(
            self.products_window, textvariable=self.data_code)
        self.entry_code.pack()

    def create_price_entry(self):
        label_price = tk.Label(self.products_window, text="Precio:")
        label_price.pack()
        self.entry_price = tk.Entry(
            self.products_window, textvariable=self.data_price)
        self.entry_price.pack()

    def create_name_entry(self):
        label_name = tk.Label(self.products_window, text='Nombre:')
        label_name.pack()
        self.entry_name = tk.Entry(
            self.products_window, textvariable=self.data_name)
        self.entry_name.pack()

    def create_stock_entry(self):
        label_stock = tk.Label(self.products_window, text="Stock:")
        label_stock.pack()
        self.entry_stock = tk.Entry(
            self.products_window, textvariable=self.data_stock)
        self.entry_stock.pack()

    def create_save_button(self):
        btn_guardar = tk.Button(
            self.products_window, text="Guardar", command=self.save_product)
        btn_guardar.pack()

    def check_duplicate_barcode(self, barcode):
        try:

            for product in self.products:
                if product[0] == barcode:
                    alert.showerror('Error', 'El codigo ya existe')
        except:
            pass

    def validate_number(self, number):
        # Verifica que stock sea un número entre 0 y 99999
        if re.match("^[0-9]{1,5}$", number):
            return int(number)
        else:
            alert.showerror(
                'Error', 'Por favor ingresa un stock válido (entre 0 y 99999)')
            return None

    def save_product(self):
        codigo = self.entry_code.get()
        nombre = self.entry_name.get()
        precio = self.entry_price.get()
        stock = self.entry_stock.get()

        if not codigo:
            alert.showerror(
                'Error', 'El campo del código de barras no puede estar vacío')
            return

        try:
            precio_validated = self.validate_number(precio)
            stock_validated = self.validate_number(stock)

            if precio_validated is not None and stock_validated is not None:
                self.check_duplicate_barcode(codigo)

                self.products.append([codigo, nombre, precio, stock])
                self.product_box.insert("", "end", values=(
                    codigo, nombre, precio, stock))

                database = Database()
                database.insert_product(codigo, nombre, precio, stock)

                self.clear_entry_fields()
        except:
            pass

    def clear_entry_fields(self):
        self.entry_code.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
