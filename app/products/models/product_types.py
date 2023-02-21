from app.db.database import Base
from sqlalchemy import Column, String
from uuid import uuid4


class ProductType(Base):
    """
       A class representing a type of product.

       :param product_type: The type of product.
       :type product_type: str
       """
    __tablename__ = "product_types"
    product_type_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    product_type = Column(String(50))

    def __init__(self, product_type):
        """
            Initialize a new instance of the ProductType class.

            :param product_type: The type of product.
            :type product_type: str
            """
        self.product_type = product_type
