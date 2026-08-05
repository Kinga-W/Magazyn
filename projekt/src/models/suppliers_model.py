from sqlalchemy import Column, Integer, String, ForeignKey, CHAR, CheckConstraint
from sqlalchemy.orm import relationship
from .base_model import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    address_id = Column(Integer, ForeignKey('address.id'), nullable=False)
    phone = Column(CHAR(11),
                   CheckConstraint("phone GLOB '[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]'"),
                   nullable=False)
    email = Column(String(255),
                   CheckConstraint("email GLOB '*?@??*.*?*'"),
                   nullable=False)

    address = relationship("Address")
