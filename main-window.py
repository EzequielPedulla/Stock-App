
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import Toplevel


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Productos')
        self.windows_styles(self.root, '800x600')

        self.menu_superior = Menu(self.root)

        self.menu_superior.add_command(label="Inicio", command=self.root)

        self.menu_superior.add_command(
            label="Productos", command=self.open_products_window)

        self.menu_superior.add_command(
            label="Ventas", command=self.open_sales_window)

        self.menu_superior.add_command(
            label="Clientes", command=self.open_clients_window)

        self.root.config(
            menu=self.menu_superior,
        )

    def windows_styles(self, window, geometry: str):
        window.geometry(geometry)
        window.configure(bg='#333')
        frame = tk.Frame(window, bg='#333')
        frame.pack(expand=True, fill='both')

    def open_products_window(self):

        products_window = Toplevel(self.root)
        products_window.title('Productos')
        self.windows_styles(products_window, '800x600')

        # Crear el Treeview
        product_box = ttk.Treeview(products_window, columns=(
            "Nombre", "Precio", "Stock"))
        product_box.heading("#0", text="Nombre")
        product_box.heading("#1", text="Precio")
        product_box.heading("#2", text="Stock")
        product_box.pack()

        # etiquetas y campos de entrada para nombre, precio y stock

        lbl_name = tk.Label(products_window, text='Nombre:')
        lbl_name.pack()
        entry_name = tk.Entry(products_window)
        entry_name.pack()

        lbl_price = tk.Label(products_window, text="Precio:")
        lbl_price.pack()

        entry_price = tk.Entry(products_window)
        entry_price.pack()

        lbl_stock = tk.Label(products_window, text="Stock:")
        lbl_stock.pack()
        entry_stock = tk.Entry(products_window)
        entry_stock.pack()

        def guardar_producto():
            nombre = entry_name.get()
            precio = entry_price.get()
            stock = entry_stock.get()
            product_box.insert("", "end", values=(nombre, precio, stock))
            # Limpiar los campos de entrada
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            entry_stock.delete(0, tk.END)

        btn_guardar = tk.Button(
            products_window, text="Guardar", command=guardar_producto)
        btn_guardar.pack()

    def open_sales_window(self):
        sales_window = Toplevel(self.root)
        sales_window.title('Ventas')
        self.windows_styles(sales_window, '800x600')

    def open_clients_window(self):
        clientes_window = Toplevel(self.root)
        clientes_window.title('Clientes')
        self.windows_styles(clientes_window, '800x600')


root = tk.Tk()
app = MainWindow(root)
root.mainloop()
