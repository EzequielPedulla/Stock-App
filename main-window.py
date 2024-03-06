
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

    def open_sales_window(self):
        sales_window = Toplevel(self.root)
        window_title = sales_window.title('Ventas')
        self.windows_styles(sales_window, '800x600')

    def open_clients_window(self):
        clientes_window = Toplevel(self.root)
        window_title = clientes_window.title('Clientes')
        self.windows_styles(clientes_window, '800x600')


root = tk.Tk()
app = MainWindow(root)
root.mainloop()
