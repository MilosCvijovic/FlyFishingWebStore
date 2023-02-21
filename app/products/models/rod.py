from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from uuid import uuid4


class Rod(Base):
    """
        Represents a fishing rod.

        :param brand: The brand of the fishing rod.
        :param model: The model of the fishing rod.
        :param length: The length of the fishing rod in feet.
        :param weight: The weight of the fishing rod in grams.
        :param AFTM: The AFTM (Association of Fishing Tackle Manufacturers) rating of the fishing rod.
        :param price: The price of the fishing rod in cents.
        :param quantity: The number of fishing rods in stock.
        :param description: A description of the fishing rod.
        :param in_stock: Whether the fishing rod is currently in stock or not.
        :param product_id: The unique identifier of the product associated with the fishing rod.
        :param product_type_id: The unique identifier of the product type associated with the fishing rod.
        """
    __tablename__ = "rods"
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
        """
            Initialize a new instance of the Rod class.

            :param brand: The brand of the rod.
            :param model: The model of the rod.
            :param length: The length of the rod in feet.
            :param weight: The weight of the rod in ounces.
            :param AFTM: The AFTM rating of the rod.
            :param price: The price of the rod in cents.
            :param quantity: The quantity of the rod in stock.
            :param description: The description of the rod.
            :param in_stock: Whether the rod is currently in stock.
            :param product_id: The ID of the product associated with the rod.
            :param product_type_id: The ID of the product type associated with the rod.
            """
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
