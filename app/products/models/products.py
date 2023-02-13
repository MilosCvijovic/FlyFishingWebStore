from app.db.database import Base
from sqlalchemy import Column, String, Integer, Float
from uuid import uuid4


class Product(Base):
    __tablename__ = "products"
    product_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    price = Column(Float)
    quantity = Column(Integer)
    description = Column(String(250))

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
