from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    code = Column(String(50), unique=True, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    number = Column(Numeric(10, 2), nullable=False)
    unit = Column(String(25), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    description = Column(Text)

    category = relationship("Category")
    supplier = relationship("Supplier")