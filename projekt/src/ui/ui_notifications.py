import tkinter as tk
from datetime import datetime
from distutils.archive_util import ARCHIVE_FORMATS
from tkinter import ttk, messagebox

from tkcalendar import DateEntry

from projekt.src.data_managers.archives_manager import ArchivesManager
from projekt.src.data_managers.categories_manager import CategoriesManager
from projekt.src.data_managers.notifications_manager import NotificationsManager
from projekt.src.data_managers.products_manager import ProductsManager
from projekt.src.data_managers.raports_manager import RaportProductsCat, RaportProductsFull, RaportTran
from projekt.src.database.database_manager import DatabaseManager


class Notifications(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.clrBackground = '#aaa'
        self.clrContainers = '#ccc'

        db_manager = DatabaseManager()
        db_manager.create_tables()

        self.cRaport = RaportProductsCat()
        self.fRaport = RaportProductsFull()
        self.tRaport = RaportTran()
        self.aManager = ArchivesManager(db_manager)
        self.nManager = NotificationsManager(db_manager)
        self.pManager = ProductsManager(db_manager)
        self.cManager = CategoriesManager(db_manager)

        self.main_notifications()

    def main_notifications(self):
        self.frmLeft = tk.Frame(self, bg=self.clrBackground, width=350)
        self.frmLeft.pack_propagate(False)
        self.frmLeft.pack(side="left", fill="y")

        self.frmRight = tk.Frame(self, bg=self.clrContainers)
        self.frmRight.pack_propagate(False)
        self.frmRight.pack(side="left", fill="both", expand=True)

        self.auto_note()

        self.create_tv_notifications()
        self.fill_tv_notifications()

        self.raport_centre()

        self.needed()
        self.fill_tv_needed(self.pManager.needed_products(20))

    def create_tv_notifications(self):
        tvNotificationsHeaders = ["date", "time", "status", "title", "description"]
        tvHeadersName = ["Data", "Godzina", "Status", "Tytuł", "Opis"]
        columnWidth = [30, 30, 60, 60, 400]
        self.tvNotifications = ttk.Treeview(self.frmRight, columns=tvNotificationsHeaders, show="headings")

        for i in range(len(tvNotificationsHeaders)):
            self.tvNotifications.column(tvNotificationsHeaders[i], width=columnWidth[i], anchor="center", stretch=True)
            self.tvNotifications.heading(tvNotificationsHeaders[i], text=tvHeadersName[i])

        self.tvNotifications.pack(fill="both", expand=True, padx=5, pady=5)

    def fill_tv_notifications(self):
        self.tvNotifications.delete(*self.tvNotifications.get_children())

        data = self.nManager.get_notifications()

        for i in data:
            self.tvNotifications.insert("", "end", values=i)



    def raport_centre(self):
        frmPanel = tk.Frame(self.frmRight, bg=self.clrBackground)
        frmPanel.pack(side="top", fill="x", padx=5, pady=5)

        frmOneP = tk.Frame(frmPanel, bg=self.clrContainers)
        frmOneP.pack(side="left", fill="y", padx=5, pady=5)
        cmbCategoriesList = self.cManager.get_categories()
        cmbCategoriesList.insert(0, "Wszystkie produkty")
        cmbCategory = ttk.Combobox(frmOneP, values=cmbCategoriesList, state="readonly")
        cmbCategory.pack(side="top", padx=5, pady=5)
        cmbCategory.set(cmbCategoriesList[0])
        btnMakeCatRaport = ttk.Button(frmOneP, text="Utwórz spis produktów", command= lambda: self.raport_prod(self.pManager.search_prod(category_id=self.cManager.get_id(cmbCategory.get())),cmbCategory.get()))
        btnMakeCatRaport.pack(side="top", padx=5, pady=5)

        frmTwoP = tk.Frame(frmPanel, bg=self.clrContainers)
        frmTwoP.pack(side="left", fill="y", padx=5, pady=5)
        lblFiltr = tk.Label(frmTwoP, bg=self.clrContainers, text="Od:")
        lblFiltr.pack(side="top", padx=5, pady=5)
        dtFrom = DateEntry(frmTwoP, width=12, date_pattern='y-mm-dd')
        dtFrom.pack(side="top", padx=5, pady=5)
        lblFiltr = tk.Label(frmTwoP, bg=self.clrContainers, text="Do:")
        lblFiltr.pack(side="top", padx=5, pady=5)
        dtTo = DateEntry(frmTwoP, width=12, date_pattern='y-mm-dd')
        dtTo.pack(side="top", padx=5, pady=5)
        btnMakeTranRaport = ttk.Button(frmTwoP, text="Utwórz spis transakcji", command= lambda: self.raport_tran(dtFrom.get(), dtTo.get()))
        btnMakeTranRaport.pack(side="top", padx=5, pady=5)

        frmThreeP = tk.Frame(frmPanel, bg=self.clrContainers)
        frmThreeP.pack(side="left", fill="x", padx=5, pady=5)
        lblFiltr = tk.Label(frmThreeP, bg=self.clrContainers, text="Szukaj:")
        lblFiltr.pack(side="left", padx=5, pady=5)

    def raport_prod(self, data, cat):
        if cat != "Wszystkie produkty":
            self.cRaport.make_file("raport_products_by_"+cat.lower()+"_", self.cRaport.generate_raport(data, cat))
        else:
            self.fRaport.make_file("raport_products_full_", self.fRaport.generate_raport(data))

    def raport_tran(self, date_from, date_to):
        date_from = datetime.strptime(date_from, "%Y-%m-%d").date()
        date_to = datetime.strptime(date_to, "%Y-%m-%d").date()
        self.tRaport.make_file("raport_transactions", self.tRaport.generate_raport(self.aManager.search_tran(date_from, date_to)))

    def needed(self):
        frmNeeded = tk.Frame(self.frmLeft, bg=self.clrContainers)
        frmNeeded.pack(fill="both", expand=True, padx=5, pady=5)
        lblCategories = tk.Label(frmNeeded, text="Wymaga dostawy")
        lblCategories.pack(fill="x", padx=5, pady=5)

        tvArchivesHeaders = ["product", "number"]
        tvHeadersName = ["Nazwa produktu", "Ilość"]
        columnWidth = [150, 5]
        self.tvNeeded = ttk.Treeview(frmNeeded, columns=tvArchivesHeaders, show="headings")

        for i in range(len(tvArchivesHeaders)):
            self.tvNeeded.column(tvArchivesHeaders[i], width=columnWidth[i], anchor="center", stretch=True)
            self.tvNeeded.heading(tvArchivesHeaders[i], text=tvHeadersName[i])

        self.tvNeeded.pack(fill="both", expand=True, padx=5, pady=5)

    def fill_tv_needed(self, data):
        self.tvNeeded.delete(*self.tvNeeded.get_children())

        for i in data:
            self.tvNeeded.insert("", "end", values=i)

    def auto_note(self):
        if len(self.pManager.needed_products(20)) > 0:
            messagebox.showinfo("Krytyczny poziom produktów w bazie", "W bazie znajdują się produkty o zbyt niskiej ilości")