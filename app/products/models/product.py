from app.db.database import Base
from sqlalchemy import Column, String, Integer
from uuid import uuid4


class Product(Base):
    """
        A class representing a product.

        :param brand: The brand of the product.
        :type brand: str
        :param model: The model of the product.
        :type model: str
        :param price: The price of the product.
        :type price: int
        """
    __tablename__ = "products"
    product_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    brand = Column(String(50))
    model = Column(String(50))
    price = Column(Integer)

    def __init__(self, brand: str, model: str, price: int):
        """
           Initialize a new instance of the Product class.

           :param brand: The brand of the product.
           :type brand: str
           :param model: The model of the product.
           :type model: str
           :param price: The price of the product.
           :type price: int
           """
        self.brand = brand
        self.model = model
        self.price = price
