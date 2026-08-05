from sqlite3 import IntegrityError

from projekt.src.models.categories_model import Category

class CategoriesManager:
    def __init__(self, db_manager):
        self._categories = []
        self.db_manager = db_manager

    def get_session(self):
        return self.db_manager.get_session()

    def get_categories(self):
        with self.get_session() as session:
            query = session.query(Category.name).all()
        return [q.name for q in query]

    def get_id(self, name):
        with self.get_session() as session:
            try:
                query = session.query(Category).where(Category.name == name).first()
                return query.id
            except AttributeError:
                return None
            except Exception as e:
                print(f"Błąd: {e}")

    def return_one_cat(self, cat):
        with (self.get_session() as session):
            q = session.query(Category).where(Category.name==cat).first()
            return q.name

    def add_cat(self, name):
        with self.get_session() as session:
            category = Category(name=name)
            try:
                session.add(category)
                session.commit()
                return ("Dodano produkt", "Pomyślnie dodano dostawce do bazy magazynu")
            except IntegrityError as e:
                session.rollback()
                print(f"Błąd: {e}")
                return ("Błąd", f"Kategoria o nazwie {name} już istnieje.")
            except Exception as e:
                session.rollback()
                print(f"Błąd: {e}")
                return ("Błąd", "Pojawił się błąd przy dodawaniu nowej kategorii")

    def edit_cat(self, cat, name):
        with self.get_session() as session:
            query = session.query(Category).where(Category.name == cat).first()
            if query is not None:
                try:
                    query.name = name
                    session.commit()
                    return 1
                except Exception as e:
                    session.rollback()
                    print(f"Błąd: {e}")
                    return 0