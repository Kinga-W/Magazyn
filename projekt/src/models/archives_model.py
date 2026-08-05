from sqlalchemy import Column, Integer, String, Numeric, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base

class Archive(Base):
    __tablename__ = 'archives'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    number = Column(Numeric(10, 2), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    operation = Column(String(20), nullable=False)
    date = Column('DATE', Date, nullable=False)
    time = Column('TIME', Time, nullable=False)

    product = relationship("Product")
    supplier = relationship("Supplier")