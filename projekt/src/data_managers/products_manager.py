from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from projekt.src.models.categories_model import Category
from projekt.src.models.suppliers_model import Supplier
from projekt.src.models.products_model import Product

class ProductsManager:
    def __init__(self, db_manager):
        self._products = []
        self.db_manager = db_manager

    @property
    def products(self):
        return self._products.copy()

    def get_session(self):
        return self.db_manager.get_session()

    def search_prod(self, search=None, sort=None, sdir="rosnąco", price=None, number=None, category_id=None, supplier_id=None):
        with self.get_session() as session:
            query = session.query(Product
                                  ).join(Category, Category.id == Product.category_id
                                  ).join(Supplier, Supplier.id == Product.supplier_id)
            if search:
                query = query.filter(
                    or_(
                        Product.name.ilike(f"%{search}%"),
                        Product.code.ilike(f"%{search}%"),
                        Product.description.ilike(f"%{search}%")
                    )
                )
            if category_id:
                query = query.filter(Product.category_id == category_id)
            if supplier_id:
                query = query.filter(Product.supplier_id == supplier_id)
            try:
                if price:
                    query = query.filter(Product.price == float(price))
                if number:
                    query = query.filter(Product.number == float(number))
            except ValueError:
                print(f"Błąd: Podano nie właściwy typ danych do wyszukiwania. Cena oraz ilość muszą być wartością liczbową.")
            if sort:
                sort = getattr(Product, sort)
                if sdir == "malejąco":
                    query = query.order_by(sort.desc())
                else:
                    query = query.order_by(sort.asc())
            query = query.all()
            return [(q.name, q.code, q.price, q.number, q.unit, q.category.name, q.supplier.name, q.description) for q in query]

    def get_products(self):
        with self.get_session() as session:
            query = session.query(Product
                                  ).join(Category, Category.id == Product.category_id
                                  ).join(Supplier, Supplier.id == Product.supplier_id
                                  ).order_by(Product.id).all()
            return [(q.name, q.code, q.price, q.number, q.unit, q.category.name, q.supplier.name, q.description) for q in query]

    def get_unique(self, category):
        with self.get_session() as session:
            uniques = session.query(getattr(Product, category)).all()
            result = sorted(list(set(i[0] for i in uniques)))
        return result

    def get_one_prod(self, prod_name):
        with self.get_session() as session:
            q = session.query(Product
                                  ).join(Category, Category.id == Product.category_id
                                  ).join(Supplier, Supplier.id == Product.supplier_id
                                  ).where(Product.name==prod_name).first()
            return [q.name, q.code, q.price, q.number, q.unit, q.category.name, q.supplier.name, q.description]

    def get_id(self, name):
        with self.get_session() as session:
            try:
                query = session.query(Product).where(Product.name == name).first()
                return query.id
            except AttributeError:
                return None
            except Exception as e:
                print(f"Błąd: {e}")

    def needed_products(self, number):
        with self.get_session() as session:
            query = session.query(Product.name, Product.number).where(Product.number<number)
            return [(q.name, q.number) for q in query]

    def delete_product(self, pname):
        with self.get_session() as session:
            product = session.query(Product).filter(Product.name == pname).first()
            if product:
                try:
                    session.delete(product)
                    session.commit()
                    print("Produkt został usunięty.")
                except Exception as e:
                    session.rollback()
                    print("Wystąpił błąd podczas usuwania produktu:", e)
            else:
                print("Produkt o podanym ID nie został znaleziony.")

    def edit_prod(self, product, name, code, price, number, unit, category, supplier, desc):
        with self.get_session() as session:
            product = session.query(Product).where(Product.name == product).first()
            if product is not None:
                try:
                    if name is not None:
                        product.name = name
                    if code is not None:
                        product.code = code
                    if float(price) > 0:
                        product.price = price
                    if float(number) >= 0:
                        product.number = number
                    product.unit = unit
                    product.category_id = category
                    product.supplier_id = supplier
                    product.description = desc
                    session.commit()
                    return 1
                except Exception as e:
                    session.rollback()
                    print(f"Błąd: {e}")
                    return 0

    def add_product(self, name, code, price, number, unit, category, supplier, desc):
        with self.get_session() as session:
            product = Product(
                name=name,
                code=code,
                price=float(price),
                number=int(number),
                unit=unit,
                category_id=category,
                supplier_id=supplier,
                description=desc
            )
            try:
                session.add(product)
                session.commit()
                return ("Dodano produkt", "Pomyślnie dodano produkt do bazy magazynu")
            except IntegrityError as e:
                session.rollback()
                print(f"Błąd: {e}")
                return ("Błąd", "Produkt o takiej nazwie lub kodzie istnieje już w bazie magazynu")
            except Exception as e:
                session.rollback()
                print(f"Błąd: {e}")
                return ("Błąd", "Pojawił się błąd przy dodawaniu produktu, sprawdź błędy pisowani oraz poprawność wszystkich podanych danych.")

