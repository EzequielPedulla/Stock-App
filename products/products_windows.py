import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import Toplevel
from tkinter import messagebox as alert
from products.database import Database


class ProductsWindow:
    def __init__(self, root):
        self.root = root
        self.products = []
        self.products_window = Toplevel(self.root)
        self.products_window.title('Productos')
        self.windows_styles(self.products_window, '800x600')
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
        if selected_item:
            item_values = self.product_box.item(selected_item)['values']
            self.product_box.delete(selected_item)
            database = Database()
            # Suponiendo que el código del producto está en la primera posición
            product_code = item_values[0]
            database.delete_product(product_code)

            self.products = [
                product for product in self.products if product[0] != product_code]
        else:
            alert.showerror(
                'Error', 'Por favor selecciona un producto para eliminar')

    def create_widgets(self):
        # Crear el Treeview
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

        button_delete = tk.Button(
            self.products_window, text='Eliminar', command=self.delete_product)
        button_delete.pack()

        def check_duplicate_barcode(self, barcode):
            for product in self.products:
                if product[0] == barcode:
                    alert.showerror('Error', 'El codigo ya existe')
                    ProductsWindow(self.root)

        def save_product():

            codigo = entry_code.get()
            nombre = entry_name.get()
            precio = entry_price.get()
            stock = entry_stock.get()

            check_duplicate_barcode(self, codigo)
            self.products.append([codigo, nombre, precio, stock])
            self.product_box.insert("", "end", values=(
                codigo, nombre, precio, stock))

            # guardar en base de datos
            database = Database()
            database.insert_product(codigo, nombre, precio, stock)
            # Limpiar los campos de entrada
            entry_code.delete(0, tk.END)
            entry_stock.delete(0, tk.END)
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            entry_stock.delete(0, tk.END)

        # etiquetas y campos de entrada para nombre, precio y stock

        data_code = IntVar()
        data_name = StringVar()
        data_price = IntVar()
        data_stock = IntVar()

        label_code = tk.Label(self.products_window, text="Codigo:")
        label_code.pack()
        entry_code = tk.Entry(self.products_window, textvariable=data_code)
        entry_code.pack()

        label_price = tk.Label(self.products_window, text="Precio:")
        label_price.pack()
        entry_price = tk.Entry(self.products_window, textvariable=data_price)
        entry_price.pack()

        label_name = tk.Label(self.products_window, text='Nombre:')
        label_name.pack()
        entry_name = tk.Entry(self.products_window, textvariable=data_name)
        entry_name.pack()

        label_stock = tk.Label(self.products_window, text="Stock:")
        label_stock.pack()
        entry_stock = tk.Entry(self.products_window, textvariable=data_stock)
        entry_stock.pack()

        btn_guardar = tk.Button(
            self.products_window, text="Guardar", command=save_product)
        btn_guardar.pack()
