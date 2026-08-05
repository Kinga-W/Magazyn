from sqlalchemy import Column, Integer, String, Date, Time, Text
from .base_model import Base

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    status = Column(String(30), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)