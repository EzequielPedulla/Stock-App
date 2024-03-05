
import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Stock App')
        self.root.geometry("1000x600")
        self.root.configure(bg='#333')
        self.frame = tk.Frame(root, bg='#333')
        self.frame.pack(expand=True, fill='both')

        self.menu_superior = Menu(self.root)

        self.menu_superior.add_command(label="Productos")
        self.menu_superior.add_command(label="Ventas")
        self.menu_superior.add_command(label="Clientes")

        self.root.config(
            menu=self.menu_superior,

        )


root = tk.Tk()
app = MainWindow(root)
root.mainloop()
