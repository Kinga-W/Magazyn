from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.util.preloaded import orm_session

from projekt.src.models import Notification

class NotificationsManager:
    def __init__(self, db_manager):
        self._notifications = []
        self.db_manager = db_manager

    @property
    def notifications(self):
        return self._notifications.copy()

    def get_session(self):
        return self.db_manager.get_session()

    def get_notifications(self):
        with self.get_session() as session:
            query = session.query(Notification).order_by(Notification.date.desc()).order_by(Notification.time.desc()).all()
            return [(q.date, q.time, q.status, q.title, q.description) for q in query]

    def add_note(self):
        with self.get_session() as session:
            note = Notification(
                date = datetime.now().date(),
                time = datetime.now().time().replace(microsecond=0),
                status = "nowe",
                title = "Krytycznie niski stan",
                description = "W bazie znajdują się produkty o zbyt niskiej ilości"
            )
            try:
                session.add(note)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Błąd: {e}")

