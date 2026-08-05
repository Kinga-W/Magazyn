from sqlite3 import IntegrityError

from projekt.src.models import Address
from projekt.src.models import Supplier

class SuppliersManager:
    def __init__(self, db_manager):
        self._suppliers = []
        self.db_manager = db_manager

    def get_session(self):
        return self.db_manager.get_session()

    def get_suppliers(self):
        with self.get_session() as session:
            query = session.query(Supplier.name).all()
        return [q.name for q in query]

    def get_id(self, name):
        with self.get_session() as session:
            try:
                query = session.query(Supplier).where(Supplier.name == name).first()
                return query.id
            except AttributeError:
                return None
            except Exception as e:
                print(f"Błąd: {e}")

    def return_one_sup(self, sup):
        with self.get_session() as session:
            q = session.query(Supplier
                                  ).join(Address, Address.id == Supplier.address_id
                                  ).where(Supplier.name==sup).first()
            return [q.name, q.phone, q.email, q.address.city, q.address.street, q.address.zip_code]

    def add_sup(self, name, phone, email, city, street, zip):
        with self.get_session() as session:
            address = Address(
                city=city,
                street=street,
                zip_code=zip
            )
            try:
                session.add(address)
                session.flush()
            except Exception as e:
                print(f"Błąd: {e}")

            supplier = Supplier(
                name=name,
                phone=phone,
                email=email,
                address_id=address.id
            )
            try:
                session.add(supplier)
                session.commit()
                return ("Dodano produkt", "Pomyślnie dodano dostawce do bazy magazynu")
            except IntegrityError as e:
                session.rollback()
                print(f"Błąd: {e}")
                return ("Błąd", f"Dostawca o nazwie {name} już istnieje.")
            except Exception as e:
                session.rollback()
                print(f"Błąd: {e}")
                return ("Błąd", "Pojawił się błąd przy dodawaniu nowego dostawcy")

    def edit_sup(self, supplier, name, phone, email, city, street, zip):
        with self.get_session() as session:
            qSupplier = session.query(Supplier).where(Supplier.name == supplier).first()
            qAddress = session.query(Address).where(Address.id == qSupplier.address_id).first()
            if qSupplier is not None:
                try:
                    if name is not None:
                        qSupplier.name = name
                    if phone is not None:
                        qSupplier.phone = phone
                    qSupplier.email = email
                    if city is not None:
                        qAddress.city = city
                    if street is not None:
                        qAddress.street = street
                    qAddress.zip_code = zip
                    session.commit()
                    return 1
                except Exception as e:
                    session.rollback()
                    print(f"Błąd: {e}")
                    return 0