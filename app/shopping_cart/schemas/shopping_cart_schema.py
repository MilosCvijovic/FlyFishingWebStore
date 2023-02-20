from typing import List

from pydantic import BaseModel
from pydantic import UUID4

from app.shopping_cart.schemas import CartItemSchema


class ShoppingCartSchema(BaseModel):
    shopping_cart_id: UUID4
    customer_id: str

    class Config:
        orm_mode = True


class ShoppingCartSchemaIn(BaseModel):
    customer_id: str

    class Config:
        orm_mode = True


class ShoppingCartSchemaOut(BaseModel):
    shopping_cart_id: str
    customer_id: str
    cart_items: List[CartItemSchema] = []
    total_price: int

    class Config:
        orm_mode = True
