from typing import List

from pydantic import BaseModel, UUID4

from app.shopping_cart.schemas import CartItemSchema


class OrderSchema(BaseModel):
    order_id: UUID4
    shopping_cart_id: str
    sent: bool = False

    class Config:
        orm_mode = True


class OrderSchemaIn(BaseModel):
    shopping_cart_id: str

    class Config:
        orm_mode = True


class OrderSchemaOut(BaseModel):
    order_id: UUID4
    sent: bool = False

    class Config:
        orm_mode = True
