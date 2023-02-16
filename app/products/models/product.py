from app.db.database import Base
from sqlalchemy import Column, String, Integer
from uuid import uuid4


class Product(Base):
    __tablename__ = "products"
    product_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    brand = Column(String(50))
    model = Column(String(50))
    price = Column(Integer)

    def __init__(self, brand: str, model: str, price: int):
        self.brand = brand
        self.model = model
        self.price = price
