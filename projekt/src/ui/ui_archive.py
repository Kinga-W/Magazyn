import tkinter as tk
from tkinter import ttk

from projekt.src.data_managers.archives_manager import ArchivesManager
from projekt.src.data_managers.products_manager import ProductsManager
from projekt.src.database.database_manager import DatabaseManager


class Archive(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.clrBackground = '#aaa'
        self.clrContainers = '#ccc'

        db_manager = DatabaseManager()

        self.aManager = ArchivesManager(db_manager)
        self.pManager = ProductsManager(db_manager)

        self.main_archive()

    def main_archive(self):
        self.frmLeft = tk.Frame(self, bg=self.clrBackground, width=350)
        self.frmLeft.pack_propagate(False)
        self.frmLeft.pack(side="left", fill="y")

        self.frmRight = tk.Frame(self, bg=self.clrContainers)
        self.frmRight.pack_propagate(False)
        self.frmRight.pack(side="left", fill="both", expand=True)

        self.searcher()
        self.create_tv_archive()
        self.fill_tv_archives(self.aManager.get_archives())

    def create_tv_archive(self):
        tvArchivesHeaders = ["date", "time", "product_name", "number", "operation", "supplier"]
        tvHeadersName = ["Data", "Godzina", "Nazwa produktu", "Zmiana", "Operacja", "Odbiorca/Dostawca"]
        columnWidth = [10, 230, 60, 40, 30, 40, 100, 75, 250]
        self.tvArchives = ttk.Treeview(self.frmRight, columns=tvArchivesHeaders, show="headings")

        for i in range(len(tvArchivesHeaders)):
            self.tvArchives.column(tvArchivesHeaders[i], width=columnWidth[i], anchor="center", stretch=True)
            self.tvArchives.heading(tvArchivesHeaders[i], text=tvHeadersName[i])

        self.tvArchives.pack(fill="both", expand=True, padx=5, pady=5)

    def fill_tv_archives(self, data):
        self.tvArchives.delete(*self.tvArchives.get_children())

        for i in data:
            self.tvArchives.insert("", "end", values=i)

    def searcher(self):
        self.frmSearcher = tk.Frame(self.frmRight, bg=self.clrContainers)
        self.frmSearcher.pack(side="top", fill="x")
        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="Szukaj:")
        self.lblFiltr.pack(side="left", padx=5, pady=(5, 0))

        cmbProductList = self.pManager.get_unique("name")
        cmbProductList.insert(0, "Wszystkie produkty")
        cmbProducts = ttk.Combobox(self.frmSearcher, values=cmbProductList, width=25, state="readonly")
        cmbProducts.pack(side="left", padx=(0, 5), pady=(5, 0))
        cmbProducts.set(cmbProductList[0])
        self.btnSearch = ttk.Button(self.frmSearcher, text="Wyszukaj", command= lambda: self.fill_tv_archives(self.aManager.search_archives_by_id(self.pManager.get_id(cmbProducts.get()))))
        self.btnSearch.pack(side="left", padx=5, pady=(5, 0))

