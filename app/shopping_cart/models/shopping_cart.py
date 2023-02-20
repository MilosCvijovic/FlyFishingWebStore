from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from uuid import uuid4


class ShoppingCart(Base):
    __tablename__ = "shopping_carts"
    shopping_cart_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)

    customer_id = Column(String(50), ForeignKey("customers.customer_id"), nullable=False)
    customer = relationship("Customer", lazy="subquery")
    total_price = Column(Integer)

    cart_items = relationship("CartItem", back_populates="shopping_cart")

    def __init__(self, customer_id: str):
        self.customer_id = customer_id
