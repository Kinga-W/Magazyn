from sqlalchemy import Column, Integer, String, CheckConstraint
from .base_model import Base

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)
    street = Column(String(120), nullable=False)
    zip_code = Column(String(6),
                      CheckConstraint("zip_code GLOB '[0-9][0-9]-[0-9][0-9][0-9]'"))

