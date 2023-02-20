from pydantic import BaseModel
from pydantic import UUID4


class CartItemSchema(BaseModel):
    cart_id: UUID4
    quantity: int
    price: int
    product_id: str
    total_price: int

    shopping_cart_id: str

    class Config:
        orm_mode = True


class CartItemSchemaIn(BaseModel):
    quantity: int
    product_id: str
    shopping_cart_id: str

    class Config:
        orm_mode = True
