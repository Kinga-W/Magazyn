from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from projekt.data.config import database_url

Base = declarative_base()

class DatabaseManager:
    def __init__(self):
        self.database_url = database_url
        self.engine = self._create_engine()
        self.session_factory = self._create_session_factory()

    def _create_engine(self):
        return create_engine(
            self.database_url,
            connect_args={"check_same_thread": False}
        )

    def _create_session_factory(self):
        return scoped_session(
            sessionmaker(bind=self.engine)
        )

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session_factory()

    def close_session(self):
        self.session_factory.remove()
