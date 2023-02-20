from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from uuid import uuid4


class CartItem(Base):
    __tablename__ = "cart_items"
    cart_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    quantity = Column(Integer)
    price = Column(Integer)
    total_price = Column(Integer, default=0)

    product_id = Column(String(50), ForeignKey("products.product_id"))
    product = relationship("Product", lazy="subquery")

    shopping_cart_id = Column(String(50), ForeignKey("shopping_carts.shopping_cart_id"))
    shopping_cart = relationship("ShoppingCart", back_populates="cart_items")

    def serialize(self):
        return {
            "cart_id": self.cart_id,
            "quantity": self.quantity,
            "price": self.price,
            "total_price": self.total_price,
            "product_id": self.product_id
        }

    def __init__(self, quantity: int, price: int, total_price: int, product_id: str, shopping_cart_id: str):
        self.quantity = quantity
        self.price = price
        self.total_price = total_price
        self.product_id = product_id
        self.shopping_cart_id = shopping_cart_id

