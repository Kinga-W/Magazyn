import tkinter as tk
from tkinter import ttk
from .ui_products import Products
from .ui_archive import Archive
from .ui_notifications import Notifications

class WarehouseUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.clrBackground = '#383838'
        self.clrContainers = '#030303'
        self.appHeight, self.appWidth = 835, 1600

        self.title("Magazyn")
        self.minsize(self.appWidth, self.appHeight)
        self.maxsize(self.appWidth, self.appHeight)
        self.configure(bg=self.clrBackground)

        style = ttk.Style().theme_use("clam")
        self.notebook()

    def notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.ProductsContent = Products(self.notebook)
        self.ArchiveContent = Archive(self.notebook)
        self.NotificationsContent = Notifications(self.notebook)

        self.notebook.add(self.ProductsContent, text="Produkty")
        self.notebook.add(self.ArchiveContent, text="Archiwum")
        self.notebook.add(self.NotificationsContent, text="Powiadomienia")