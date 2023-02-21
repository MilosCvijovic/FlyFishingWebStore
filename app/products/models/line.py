from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from uuid import uuid4


class Line(Base):
    """A class representing a fishing line.

       :param brand: The brand of the line.
       :param model: The model of the line.
       :param length: The length of the line.
       :param AFTM: The AFTM (American Fishing Tackle Manufacturers Association) rating of the line.
       :param price: The price of the line.
       :param quantity: The quantity of the line in stock.
       :param description: A description of the line.
       :param in_stock: Whether the line is currently in stock.
       :param product_id: The ID of the product associated with the line.
       :param product_type_id: The ID of the product type associated with the line.
       """
    __tablename__ = "lines"
    line_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    brand = Column(String(50))
    model = Column(String(50))
    length = Column(Integer)
    AFTM = Column(String(10))
    price = Column(Integer)
    quantity = Column(Integer)
    description = Column(String(250))
    in_stock = Column(Boolean, default=True)

    product_id = Column(String(50), ForeignKey("products.product_id"))
    product = relationship("Product", lazy="subquery")

    product_type_id = Column(String(50), ForeignKey("product_types.product_type_id"))
    product_type = relationship("ProductType", lazy="subquery")

    def __init__(self, brand: str, model: str, length: int, AFTM: str, price: int,
                 quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Initialize a new instance of the Line class.

            :param brand: The brand of the line.
            :type brand: str
            :param model: The model of the line.
            :type model: str
            :param length: The length of the line in feet.
            :type length: int
            :param AFTM: The weight designation of the line according to the AFTM system.
            :type AFTM: str
            :param price: The price of the line in cents.
            :type price: int
            :param quantity: The number of lines available in stock.
            :type quantity: int
            :param description: A description of the line.
            :type description: str
            :param in_stock: Whether the line is in stock or not.
            :type in_stock: bool
            :param product_id: The ID of the associated product.
            :type product_id: str
            :param product_type_id: The ID of the associated product type.
            :type product_type_id: str
            """
        self.brand = brand
        self.model = model
        self.length = length
        self.AFTM = AFTM
        self.price = price
        self.quantity = quantity
        self.description = description
        self.in_stock = in_stock
        self.product_id = product_id
        self.product_type_id = product_type_id
