from sqlalchemy import or_, and_
from datetime import date, time, datetime
from decimal import Decimal

from projekt.src.models import Archive, Product, Supplier


class ArchivesManager:
    def __init__(self, db_manager):
        self._archives = []
        self.db_manager = db_manager

    @property
    def archives(self):
        return self._archives.copy()

    def get_session(self):
        return self.db_manager.get_session()

    def get_archives(self):
        with (self.get_session() as session):
            query = session.query(Archive
                                ).join(Product
                                ).join(Supplier
                                ).order_by(Archive.date.desc()).order_by(Archive.time.desc()).all()
            return [(q.date, q.time, q.product.name, q.number, q.operation, q.supplier.name) for q in query]

    def search_archives_by_id(self, product_id):
        with self.get_session() as session:
            if product_id is not None:
                query = session.query(Archive).join(Product).join(Supplier).where(Archive.product_id == product_id).all()
            else:
                query = session.query(Archive).join(Product).join(Supplier).all()
            return [(q.date, q.time, q.product.name, q.number, q.operation, q.supplier.name) for q in query]

    def search_tran(self, date_from, date_to):
        with self.get_session() as session:
            query = session.query(Archive).filter(Archive.date.between(date_from, date_to)).order_by(Archive.date.desc()).order_by(Archive.time.desc()).all()
            return [(q.date, q.time, q.product.name, q.number, q.operation, q.supplier.name) for q in query]


    def add_archive(self, product_id, number, supplier_id, operation, change_date=None, change_time=None):
        with self.get_session() as session:
            try:
                new_change = Archive(
                    product_id=product_id,
                    number=Decimal(number),
                    supplier_id=supplier_id,
                    operation=operation,
                    date=change_date or date.today(),
                    time=change_time or datetime.now().time()
                )
                session.add(new_change)
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                print(f"Błąd podczas dodawania zmiany: {e}")
                return False