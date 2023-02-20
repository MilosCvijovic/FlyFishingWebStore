from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from uuid import uuid4


class Fly(Base):
    __tablename__ = "flies"
    rod_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    brand = Column(String(50))
    model = Column(String(50))
    length = Column(Integer)
    weight = Column(Integer)
    AFTM = Column(String(10))
    price = Column(Integer)
    quantity = Column(Integer)
    description = Column(String(250))
    in_stock = Column(Boolean, default=True)

    product_id = Column(String(50), ForeignKey("products.product_id"))
    product = relationship("Product", lazy="subquery")

    product_type_id = Column(String(50), ForeignKey("product_types.product_type_id"))
    product_type = relationship("ProductType", lazy="subquery")

    def __init__(self, brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                 quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        self.brand = brand
        self.model = model
        self.length = length
        self.weight = weight
        self.AFTM = AFTM
        self.price = price
        self.quantity = quantity
        self.description = description
        self.in_stock = in_stock
        self.product_id = product_id
        self.product_type_id = product_type_id
