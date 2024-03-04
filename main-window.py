
import tkinter as tk


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Stock App')


root = tk.Tk()
app = MainWindow(root)
root.mainloop()
