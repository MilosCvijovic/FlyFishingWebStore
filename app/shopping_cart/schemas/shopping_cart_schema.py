from typing import List

from pydantic import BaseModel
from pydantic import UUID4

from app.shopping_cart.schemas import CartItemSchema


class ShoppingCartSchema(BaseModel):
    """Schema class for a shopping cart."""
    shopping_cart_id: UUID4
    customer_id: str

    class Config:
        orm_mode = True


class ShoppingCartSchemaIn(BaseModel):
    """Schema class for creating a shopping cart."""
    customer_id: str

    class Config:
        orm_mode = True


class ShoppingCartSchemaOut(BaseModel):
    """Schema class for retrieving a shopping cart."""
    shopping_cart_id: str
    customer_id: str
    cart_items: List[CartItemSchema] = []
    total_price: int

    class Config:
        orm_mode = True
