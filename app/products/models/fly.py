from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from uuid import uuid4


class Fly(Base):
    """
        A class representing a fly product in the inventory.

        :param brand: The brand of the fly.
        :type brand: str
        :param model: The model of the fly.
        :type model: str
        :param length: The length of the fly.
        :type length: int
        :param weight: The weight of the fly.
        :type weight: int
        :param price: The price of the fly.
        :type price: int
        :param quantity: The quantity of the fly in stock.
        :type quantity: int
        :param description: A description of the fly.
        :type description: str
        :param in_stock: Whether the fly is in stock or not.
        :type in_stock: bool
        :param product_id: The ID of the product associated with the fly.
        :type product_id: str
        :param product_type_id: The ID of the product type associated with the fly.
        :type product_type_id: str
        """
    __tablename__ = "flies"
    fly_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    brand = Column(String(50))
    model = Column(String(50))
    length = Column(Integer)
    weight = Column(Integer)
    price = Column(Integer)
    quantity = Column(Integer)
    description = Column(String(250))
    in_stock = Column(Boolean, default=True)

    product_id = Column(String(50), ForeignKey("products.product_id"))
    product = relationship("Product", lazy="subquery")

    product_type_id = Column(String(50), ForeignKey("product_types.product_type_id"))
    product_type = relationship("ProductType", lazy="subquery")

    def __init__(self, brand: str, model: str, length: int, weight: int, price: int,
                 quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Initializes a new instance of the Fly class.

            :param brand: The brand of the fly.
            :type brand: str
            :param model: The model of the fly.
            :type model: str
            :param length: The length of the fly.
            :type length: int
            :param weight: The weight of the fly.
            :type weight: int
            :param price: The price of the fly.
            :type price: int
            :param quantity: The quantity of the fly in stock.
            :type quantity: int
            :param description: A description of the fly.
            :type description: str
            :param in_stock: Whether the fly is in stock or not.
            :type in_stock: bool
            :param product_id: The ID of the product associated with the fly.
            :type product_id: str
            :param product_type_id: The ID of the product type associated with the fly.
            :type product_type_id: str
            """
        self.brand = brand
        self.model = model
        self.length = length
        self.weight = weight
        self.price = price
        self.quantity = quantity
        self.description = description
        self.in_stock = in_stock
        self.product_id = product_id
        self.product_type_id = product_type_id
