from uuid import uuid4

from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Boolean


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)

    shopping_cart_id = Column(String(50), ForeignKey("shopping_carts.shopping_cart_id"))
    shopping_cart = relationship("ShoppingCart", lazy="subquery")

    sent = Column(Boolean, default=False)

    def __init__(self, shopping_cart_id: str, sent: bool = False):
        self.shopping_cart_id = shopping_cart_id
        self.sent = sent


