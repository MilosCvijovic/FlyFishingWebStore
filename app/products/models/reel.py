from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from uuid import uuid4


class Reel(Base):
    """
        A class representing a reel in the system.

        :param brand: The brand of the reel.
        :type brand: str
        :param model: The model of the reel.
        :type model: str
        :param weight: The weight of the reel.
        :type weight: int
        :param AFTM: The AFTM rating of the reel.
        :type AFTM: str
        :param price: The price of the reel.
        :type price: int
        :param quantity: The quantity of the reel in stock.
        :type quantity: int
        :param description: The description of the reel.
        :type description: str
        :param in_stock: A boolean representing whether the reel is in stock.
        :type in_stock: bool
        :param product_id: The ID of the product that the reel belongs to.
        :type product_id: str
        :param product_type_id: The ID of the product type that the reel belongs to.
        :type product_type_id: str
        """
    __tablename__ = "reels"
    reel_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    brand = Column(String(50))
    model = Column(String(50))
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

    def __init__(self, brand: str, model: str, weight: int, AFTM: str, price: int,
                 quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Initializes a new instance of the Reel class.

            :param brand: The brand of the reel.
            :type brand: str
            :param model: The model of the reel.
            :type model: str
            :param weight: The weight of the reel.
            :type weight: int
            :param AFTM: The AFTM (Association of Fishing Tackle Manufacturers) rating of the reel.
            :type AFTM: str
            :param price: The price of the reel.
            :type price: int
            :param quantity: The quantity of the reel in stock.
            :type quantity: int
            :param description: A description of the reel.
            :type description: str
            :param in_stock: A flag indicating whether the reel is in stock.
            :type in_stock: bool
            :param product_id: The ID of the product to which this reel belongs.
            :type product_id: str
            :param product_type_id: The ID of the product type to which this reel belongs.
            :type product_type_id: str
            """
        self.brand = brand
        self.model = model
        self.weight = weight
        self.AFTM = AFTM
        self.price = price
        self.quantity = quantity
        self.description = description
        self.in_stock = in_stock
        self.product_id = product_id
        self.product_type_id = product_type_id
