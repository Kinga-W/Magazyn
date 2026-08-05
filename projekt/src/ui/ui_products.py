import tkinter as tk
from tkinter import ttk, messagebox

from projekt.src.data_managers.archives_manager import ArchivesManager
from projekt.src.data_managers.products_manager import ProductsManager
from projekt.src.data_managers.categories_manager import CategoriesManager
from projekt.src.data_managers.suppliers_manager import SuppliersManager
from projekt.src.database.database_manager import DatabaseManager

class Products(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.clrBackground = '#aaa'
        self.clrContainers = '#ccc'

        db_manager = DatabaseManager()
        db_manager.create_tables()

        self.aManager = ArchivesManager(db_manager)
        self.pManager = ProductsManager(db_manager)
        self.cManager = CategoriesManager(db_manager)
        self.sManager = SuppliersManager(db_manager)

        self.main_products()

    def main_products(self):
        self.frmLeft = tk.Frame(self, bg=self.clrBackground, width=350)
        self.frmLeft.pack_propagate(False)
        self.frmLeft.pack(side="left", fill="y")

        self.frmRight = tk.Frame(self, bg=self.clrContainers)
        self.frmRight.pack_propagate(False)
        self.frmRight.pack(side="left", fill="both", expand=True)

        self.cmbUnitList = ["sztuka", "litr", "kilogram"]
        self.cmbCategoriesList = self.cManager.get_categories()
        self.cmbSuppliersList = self.sManager.get_suppliers()

        self.create_add()
        self.create_edit_form()
        self.create_edit()

        self.create_tv_products()
        self.fill_tv_products(self.pManager.get_products())

        self.searcher()

        self.suppliers()
        self.categories()

    def create_add(self):
        self.lblAdd = tk.Label(self.frmRight, text="Dodawanie produktu:")

        self.frmAdd = tk.Frame(self.frmRight)
        self.frmAdd.pack(side="bottom", fill="x")
        self.entName = ttk.Entry(self.frmAdd, width=30)
        self.entName.pack(side="left", padx=5, pady=5)
        self.entCode = ttk.Entry(self.frmAdd, width=15)
        self.entCode.pack(side="left", padx=5, pady=5)
        self.entPrice = ttk.Entry(self.frmAdd, width=10)
        self.entPrice.pack(side="left", padx=5, pady=5)
        self.entNumber = ttk.Entry(self.frmAdd, width=10)
        self.entNumber.pack(side="left", padx=5, pady=5)

        self.cmbUnit = ttk.Combobox(self.frmAdd, values=self.cmbUnitList, state="readonly", width=10)
        self.cmbUnit.pack(side="left", padx=5, pady=5)

        self.cmbCategory = ttk.Combobox(self.frmAdd, values=self.cmbCategoriesList, state="readonly")
        self.cmbCategory.pack(side="left", padx=5, pady=5)

        self.cmbSupplier = ttk.Combobox(self.frmAdd, values=self.cmbSuppliersList, state="readonly")
        self.cmbSupplier.pack(side="left", padx=5, pady=5)

        self.entDescription = ttk.Entry(self.frmAdd, width=45)
        self.entDescription.pack(side="left", padx=5, pady=5)

        self.btnAdd = ttk.Button(self.frmAdd, text="Dodaj produkt", command= lambda: self.popup_add(self.entName.get(), self.entCode.get(), self.entPrice.get(), self.entNumber.get(), self.cmbUnit.get(), self.cmbCategory.get(), self.cmbSupplier.get(), self.entDescription.get()))
        self.btnAdd.pack(side="left", padx=5, pady=5)

        self.lblAdd.pack(side="bottom", fill="x")

    def clear_edits(self):
        self.entNameE.delete(0, tk.END)
        self.entCodeE.delete(0, tk.END)
        self.entPriceE.delete(0, tk.END)
        self.entNumberE.delete(0, tk.END)
        self.cmbUnitE.set("")
        self.cmbCategoryE.set("")
        self.cmbSupplierE.set("")
        self.entDescriptionE.delete(0, tk.END)

    def fill_edits(self):
        found = self.pManager.get_one_prod(self.cmbChoice.get())
        self.clear_edits()
        self.entNameE.insert(0, found[0])
        self.entCodeE.insert(0, found[1])
        self.entPriceE.insert(0, found[2])
        self.entNumberE.insert(0, found[3])
        self.cmbUnitE.set(found[4])
        self.cmbCategoryE.set(found[5])
        self.cmbSupplierE.set(found[6])
        self.entDescriptionE.insert(0, found[7])

    def create_edit(self):
        self.frmEdit = tk.Frame(self.frmRight)
        self.frmEdit.pack(side="bottom", fill="x")

        self.txtChoice = ttk.Label(self.frmEdit, text="Wybierz produkt i akcje:")
        self.txtChoice.pack(side="left", padx=5, pady=(5,0))

        self.cmbChoiceList = self.pManager.get_unique("name")
        self.cmbChoice = ttk.Combobox(self.frmEdit, values=self.cmbChoiceList, state="readonly", width=40)
        self.cmbChoice.pack(side="left", padx=5, pady=(5,0))
        self.btnChoice = ttk.Button(self.frmEdit, text="Wybierz", command= lambda: self.fill_edits())
        self.btnChoice.pack(side="left", padx=5, pady=(5,0))
        self.btnDelete = ttk.Button(self.frmEdit, text="Usuń", command= lambda: self.popup_delete(self.cmbChoice.get()))
        self.btnDelete.pack(side="left", padx=5, pady=(5, 0))
        self.btnClear = ttk.Button(self.frmEdit, text="Wyczyść", command=lambda: self.clear_edits())
        self.btnClear.pack(side="left", padx=5, pady=(5, 0))

    def create_edit_form(self):
        self.frmEditForm = tk.Frame(self.frmRight)
        self.frmEditForm.pack(side="bottom", fill="x")
        self.entNameE = ttk.Entry(self.frmEditForm, width=30)
        self.entNameE.pack(side="left", padx=5, pady=5)
        self.entCodeE = ttk.Entry(self.frmEditForm, width=15)
        self.entCodeE.pack(side="left", padx=5, pady=5)
        self.entPriceE = ttk.Entry(self.frmEditForm, width=10)
        self.entPriceE.pack(side="left", padx=5, pady=5)
        self.entNumberE = ttk.Entry(self.frmEditForm, width=10)
        self.entNumberE.pack(side="left", padx=5, pady=5)

        self.cmbUnitE = ttk.Combobox(self.frmEditForm, values=self.cmbUnitList, state="readonly", width=10)
        self.cmbUnitE.pack(side="left", padx=5, pady=5)

        self.cmbCategoryE = ttk.Combobox(self.frmEditForm, values=self.cmbCategoriesList, state="readonly")
        self.cmbCategoryE.pack(side="left", padx=5, pady=5)

        self.cmbSupplierE = ttk.Combobox(self.frmEditForm, values=self.cmbSuppliersList, state="readonly")
        self.cmbSupplierE.pack(side="left", padx=5, pady=5)

        self.entDescriptionE = ttk.Entry(self.frmEditForm, width=45)
        self.entDescriptionE.pack(side="left", padx=5, pady=5)
        self.btnEdit = ttk.Button(self.frmEditForm, text="Edytuj", command= lambda: self.popup_edit(self.cmbChoice.get(), self.entNameE.get(), self.entCodeE.get(), self.entPriceE.get(), self.entNumberE.get(), self.cmbUnitE.get(), self.cmbCategoryE.get(), self.cmbSupplierE.get(), self.entDescriptionE.get()))
        self.btnEdit.pack(side="left", padx=5, pady=(5, 0))


    def create_tv_products(self):
        tvProductsHeaders = ["name", "code", "price", "number", "unit", "category", "supplier", "description"]
        tvHeadersName = ["Nazwa produktu", "Kod", "Cena", "Ilość", "Jednostka", "Kategoria", "Dostawca", "Opis"]
        columnWidth = [230, 60, 40, 30, 40, 100, 75, 250]
        self.tvProducts = ttk.Treeview(self.frmRight, columns=tvProductsHeaders, show="headings")

        for i in range(len(tvProductsHeaders)):
            self.tvProducts.column(tvProductsHeaders[i], width=columnWidth[i], anchor="center", stretch=True)
            self.tvProducts.heading(tvProductsHeaders[i], text=tvHeadersName[i])

        self.tvProducts.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

    def fill_tv_products(self, data):
        self.tvProducts.delete(*self.tvProducts.get_children())

        for i in data:
            self.tvProducts.insert("", "end", values=i)

    def popup_delete(self, product):
        if product == "" or None:
            messagebox.showinfo("Błąd", "Nie wybrano produktu do usunięcia")
            return
        answer = messagebox.askyesno("Potwierdź usunięcie produktu", f"Czy napewno chcesz usunąć {product}?")
        if answer:
            self.pManager.delete_product(product)
            self.clear_edits()
            self.fill_tv_products(self.pManager.get_products())

            self.cmbChoiceList = self.pManager.get_unique("name")
            self.cmbChoice['values'] = self.cmbChoiceList
            self.cmbChoice.set('')

    def popup_edit(self, product, name, code, price, number, unit, category, supplier, desc):
        if product == "" or None:
            messagebox.showinfo("Błąd", "Nie wybrano produktu do edycji")
            return
        answer = messagebox.askyesno("Potwierdź zmiany", f"Czy napewno chcesz zamienić {product} na {name}, {code}, {price}, {number}, {unit}, {category}, {supplier}, {desc}?")
        if answer:
            if self.pManager.edit_prod(product, name, code, price, number, unit, self.cManager.get_id(category), self.sManager.get_id(supplier), desc):
                self.clear_edits()
                self.fill_tv_products(self.pManager.get_products())
                #self.aManager.add_archive(product_id, number, supplier_id, operation, change_date=None, change_time=None)

                self.cmbChoiceList = self.pManager.get_unique("name")
                self.cmbChoice['values'] = self.cmbChoiceList
                self.cmbChoice.set('')
            else:
                messagebox.showinfo("Błąd", f"Nie udało się zedytować {product}, sprawdź błędy pisowani oraz poprawność wszystkich podanych danych.")

    def popup_add(self, name, code, price, number, unit, category, supplier, desc):
        result = self.pManager.add_product(name, code, price, number, unit, self.cManager.get_id(category), self.sManager.get_id(supplier), desc)
        messagebox.showinfo(result[0], result[1])
        if result[0] == "Błąd":
            return
        self.clear_edits()
        self.fill_tv_products(self.pManager.get_products())
        self.cmbChoiceList = self.pManager.get_unique("name")
        self.cmbChoice['values'] = self.cmbChoiceList
        self.cmbChoice.set('')

    def searcher(self):
        self.frmSearcher = tk.Frame(self.frmRight, bg=self.clrContainers, height=100)
        self.frmSearcher.pack(side="bottom", fill="x")
        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="Szukaj:")
        self.lblFiltr.pack(side="left", padx=5, pady=(5,0))
        self.entSearcher = ttk.Entry(self.frmSearcher, width=30)
        self.entSearcher.pack(side="left", padx=5, pady=(5,0))
        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="Sortuj:")
        self.lblFiltr.pack(side="left", padx=5, pady=(5,0))
        self.cmbSort = ttk.Combobox(self.frmSearcher, values=["nazwa", "kod", "cena", "ilość"], width=7, state="readonly")
        self.cmbSort.pack(side="left", padx=5, pady=(5,0))
        self.cmbDirection = ttk.Combobox(self.frmSearcher, values=["rosnąco", "malejąco"], width=10, state="readonly")
        self.cmbDirection.pack(side="left", padx=5, pady=(5,0))

        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="Filtruj:")
        self.lblFiltr.pack(side="left", padx=5, pady=(5,0))
        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="cena:")
        self.lblFiltr.pack(side="left", padx=0, pady=(5, 0))
        self.entPrice = ttk.Entry(self.frmSearcher, width=7)
        self.entPrice.pack(side="left", padx=(0,5), pady=(5, 0))
        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="ilość:")
        self.lblFiltr.pack(side="left", padx=0, pady=(5, 0))
        self.entNumber = ttk.Entry(self.frmSearcher, width=7)
        self.entNumber.pack(side="left", padx=(0, 5), pady=(5, 0))
        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="kategoria:")
        self.lblFiltr.pack(side="left", padx=0, pady=(5, 0))
        self.cmbCat = ttk.Combobox(self.frmSearcher, values=self.cmbCategoriesList, width=17, state="readonly")
        self.cmbCat.pack(side="left", padx=(0,5), pady=(5, 0))
        self.lblFiltr = tk.Label(self.frmSearcher, bg=self.clrContainers, text="dostawca:")
        self.lblFiltr.pack(side="left", padx=0, pady=(5, 0))
        self.cmbSup = ttk.Combobox(self.frmSearcher, values=self.cmbSuppliersList, width=15, state="readonly")
        self.cmbSup.pack(side="left", padx=(0,5), pady=(5, 0))

        self.btnSearch = ttk.Button(self.frmSearcher, text="Wyszukaj", command= lambda: self.fill_tv_products(self.pManager.search_prod(
            self.entSearcher.get(), self.search_enabler(self.cmbSort.get()), self.cmbDirection.get(),
            self.entPrice.get(), self.entNumber.get(), self.cManager.get_id(self.cmbCat.get()), self.sManager.get_id(self.cmbSup.get()))))
        self.btnSearch.pack(side="left", padx=5, pady=(5,0))

        self.btnClear = ttk.Button(self.frmSearcher, text="Wyczyść", command=lambda: self.clear_searcher())
        self.btnClear.pack(side="left", padx=5, pady=(5, 0))

    def search_enabler(self, sort=None):
        if sort == "nazwa":
            return "name"
        if sort == "kod":
            return "code"
        if sort == "cena":
            return "price"
        if sort == "ilość":
            return "number"

    def clear_searcher(self):
        self.entSearcher.delete(0, tk.END)
        self.cmbSort.set("")
        self.cmbDirection.set("")
        self.entPrice.delete(0, tk.END)
        self.entNumber.delete(0, tk.END)
        self.cmbCat.set("")
        self.cmbSup.set("")

    def suppliers(self):
        frmSups = tk.Frame(self.frmLeft, bg=self.clrContainers)
        frmSups.pack(fill="x", padx=5, pady=5)
        lblSuppliers = tk.Label(frmSups, text="Dowstawcy")
        lblSuppliers.pack(fill="x", padx=5, pady=5)
        lblSuppliers = tk.Label(frmSups, text="Wybierz dostawce", bg=self.clrContainers)
        lblSuppliers.pack(fill="x", padx=5, pady=(5,0))
        self.cmbSups = ttk.Combobox(frmSups, values=self.cmbSuppliersList, width=30, state="readonly")
        self.cmbSups.pack(side="top", padx=5, pady=(5,0))
        btnChoose = ttk.Button(frmSups, width=30, text="Wybierz", command= lambda: self.fill_sups(self.cmbSups.get()))
        btnChoose.pack(side="top", padx=5, pady=5)

        lblSuppliers = tk.Label(frmSups, text="Nazwa", bg=self.clrContainers)
        lblSuppliers.pack(fill="x", padx=5, pady=(5,0))
        self.entSupName = ttk.Entry(frmSups, width=30)
        self.entSupName.pack(side="top", padx=5, pady=(5, 0))
        lblSuppliers = tk.Label(frmSups, text="Numer telefonu", bg=self.clrContainers)
        lblSuppliers.pack(fill="x", padx=5, pady=(5,0))
        self.entSupTel = ttk.Entry(frmSups, width=30)
        self.entSupTel.pack(side="top", padx=5, pady=(5,0))
        lblSuppliers = tk.Label(frmSups, text="Email", bg=self.clrContainers)
        lblSuppliers.pack(fill="x", padx=5, pady=(5, 0))
        self.entSupMail = ttk.Entry(frmSups, width=30)
        self.entSupMail.pack(side="top", padx=5, pady=(5, 0))
        lblSuppliers = tk.Label(frmSups, text="Miasto", bg=self.clrContainers)
        lblSuppliers.pack(fill="x", padx=5, pady=(5, 0))
        self.entSupCity = ttk.Entry(frmSups, width=30)
        self.entSupCity.pack(side="top", padx=5, pady=(5, 0))
        lblSuppliers = tk.Label(frmSups, text="Ulica i numer", bg=self.clrContainers)
        lblSuppliers.pack(fill="x", padx=5, pady=(5, 0))
        self.entSupStreet = ttk.Entry(frmSups, width=30)
        self.entSupStreet.pack(side="top", padx=5, pady=(5, 0))
        lblSuppliers = tk.Label(frmSups, text="Kod pocztowy", bg=self.clrContainers)
        lblSuppliers.pack(fill="x", padx=5, pady=(5, 0))
        self.entSupCode = ttk.Entry(frmSups, width=30)
        self.entSupCode.pack(side="top", padx=5, pady=5)

        btnSupAdd = ttk.Button(frmSups, width=30, text="Dodaj dostawce", command= lambda: self.popup_add_sup())
        btnSupAdd.pack(side="top", padx=5, pady=5)
        btnSupEdit = ttk.Button(frmSups, width=30, text="Edytuj wybranego dostawce", command= lambda: self.popup_edit_sup(self.cmbSups.get(),
            self.entSupName.get(), self.entSupTel.get(), self.entSupMail.get(), self.entSupCity.get(), self.entSupStreet.get(), self.entSupCode.get()))
        btnSupEdit.pack(side="top", padx=5, pady=5)

    def fill_sups(self, sup):
        found = self.sManager.return_one_sup(sup)
        self.clear_sups()
        self.entSupName.insert(0, found[0])
        self.entSupTel.insert(0, found[1])
        self.entSupMail.insert(0, found[2])
        self.entSupCity.insert(0, found[3])
        self.entSupStreet.insert(0, found[4])
        self.entSupCode.insert(0, found[5])

    def clear_sups(self):
        self.entSupName.delete(0, tk.END)
        self.entSupTel.delete(0, tk.END)
        self.entSupMail.delete(0, tk.END)
        self.entSupCity.delete(0, tk.END)
        self.entSupStreet.delete(0, tk.END)
        self.entSupCode.delete(0, tk.END)

    def popup_add_sup(self):
        result = self.sManager.add_sup(
            self.entSupName.get(), self.entSupTel.get(), self.entSupMail.get(), self.entSupCity.get(), self.entSupStreet.get(), self.entSupCode.get())
        messagebox.showinfo(result[0], result[1])
        if result[0] == "Błąd":
            return
        self.clear_sups()
        self.fill_tv_products(self.pManager.get_products())
        self.cmbSuppliersList = self.sManager.get_suppliers()
        self.cmbSupplier['values'] = self.cmbSuppliersList
        self.cmbSupplierE['values'] = self.cmbSuppliersList
        self.cmbSups['values'] = self.cmbSuppliersList
        self.cmbSup['values'] = self.cmbSuppliersList

    def popup_edit_sup(self, supplier, name, phone, email, city, street, zip):
        if supplier == "" or None:
            messagebox.showinfo("Błąd", "Nie wybrano dostawcy do edycji")
            return
        answer = messagebox.askyesno("Potwierdź zmiany", f"Czy napewno chcesz zamienić {supplier} na {name}, {phone}, {email}, {city}, {street}, {zip}?")
        if answer:
            if self.sManager.edit_sup(supplier, name, phone, email, city, street, zip):
                self.clear_sups()
                self.fill_tv_products(self.pManager.get_products())
                self.cmbSuppliersList = self.sManager.get_suppliers()
                self.cmbSupplier['values'] = self.cmbSuppliersList
                self.cmbSupplierE['values'] = self.cmbSuppliersList
                self.cmbSups['values'] = self.cmbSuppliersList
                self.cmbSup['values'] = self.cmbSuppliersList
            else:
                messagebox.showinfo("Błąd", f"Nie udało się zedytować {supplier}, sprawdź błędy pisowani oraz poprawność wszystkich podanych danych.")

    def categories(self):
        frmCats = tk.Frame(self.frmLeft, bg=self.clrContainers)
        frmCats.pack(fill="x", padx=5, pady=(0, 5))
        lblCategories = tk.Label(frmCats, text="Kategorie")
        lblCategories.pack(fill="x", padx=5, pady=5)
        lblCategories = tk.Label(frmCats, text="Wybierz kategorie", bg=self.clrContainers)
        lblCategories.pack(fill="x", padx=5, pady=(5, 0))
        self.cmbCats = ttk.Combobox(frmCats, values=self.cmbCategoriesList, width=30, state="readonly")
        self.cmbCats.pack(side="top", padx=5, pady=(5, 0))
        btnChoose = ttk.Button(frmCats, width=30, text="Wybierz", command=lambda: self.entCatName.insert(0, (self.cmbCats.get())))
        btnChoose.pack(side="top", padx=5, pady=5)

        lblCategories = tk.Label(frmCats, text="Nazwa", bg=self.clrContainers)
        lblCategories.pack(fill="x", padx=5, pady=(5, 0))
        self.entCatName = ttk.Entry(frmCats, width=30)
        self.entCatName.pack(side="top", padx=5, pady=5)

        btnCatAdd = ttk.Button(frmCats, width=30, text="Dodaj kategorie", command=lambda: self.popup_add_cat())
        btnCatAdd.pack(side="top", padx=5, pady=5)
        btnCatEdit = ttk.Button(frmCats, width=30, text="Edytuj wybraną kategorie", command= lambda: self.popup_edit_cat(self.cmbCats.get(), self.entCatName.get()))
        btnCatEdit.pack(side="top", padx=5, pady=(5,10))

    def popup_add_cat(self):
        result = self.cManager.add_cat(self.entCatName.get())
        messagebox.showinfo(result[0], result[1])
        if result[0] == "Błąd":
            return
        self.entCatName.delete(0, tk.END)
        self.fill_tv_products(self.pManager.get_products())
        self.cmbCategoriesList = self.cManager.get_categories()
        self.cmbCategoryE['values'] = self.cmbCategoriesList
        self.cmbCategory['values'] = self.cmbCategoriesList
        self.cmbCats['values'] = self.cmbCategoriesList
        self.cmbCat['values'] = self.cmbCategoriesList

    def popup_edit_cat(self, cat, name):
        if cat == "" or None:
            messagebox.showinfo("Błąd", "Nie wybrano kategorii do edycji")
            return
        answer = messagebox.askyesno("Potwierdź zmiany",
                                     f"Czy napewno chcesz zamienić {cat} na {name}?")
        if answer:
            if self.cManager.edit_cat(cat, name):
                self.entCatName.delete(0, tk.END)
                self.fill_tv_products(self.pManager.get_products())
                self.cmbCategoriesList = self.cManager.get_categories()
                self.cmbCategoryE['values'] = self.cmbCategoriesList
                self.cmbCategory['values'] = self.cmbCategoriesList
                self.cmbCats['values'] = self.cmbCategoriesList
                self.cmbCat['values'] = self.cmbCategoriesList
            else:
                messagebox.showinfo("Błąd",
                                    f"Nie udało się zedytować {cat}, sprawdź błędy pisowani oraz poprawność wszystkich podanych danych.")

