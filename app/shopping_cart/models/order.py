from uuid import uuid4

from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Boolean


class Order(Base):
    """
        A class representing an order in the system.
        """
    __tablename__ = "orders"
    order_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)

    shopping_cart_id = Column(String(50), ForeignKey("shopping_carts.shopping_cart_id"))
    shopping_cart = relationship("ShoppingCart", lazy="subquery")

    sent = Column(Boolean, default=False)

    def __init__(self, shopping_cart_id: str, sent: bool = False):
        """
            Initialize a new instance of the Order class.

            :param shopping_cart_id: The ID of the shopping cart associated with the order.
            :param sent: A boolean value indicating whether the order has been sent.
            """
        self.shopping_cart_id = shopping_cart_id
        self.sent = sent
