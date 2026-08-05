from sqlalchemy import Column, Integer, String
from .base_model import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)

