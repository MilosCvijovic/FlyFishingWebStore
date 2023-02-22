from pydantic import BaseModel
from pydantic import UUID4


class CartItemSchema(BaseModel):
    """Schema for CartItem model with fields that are returned in API responses."""
    cart_id: UUID4
    quantity: int
    price: int
    product_id: str
    total_price: int

    shopping_cart_id: str

    class Config:
        orm_mode = True


class CartItemSchemaIn(BaseModel):
    """Schema for CartItem model with fields that are accepted in API requests."""
    quantity: int
    product_id: str
    shopping_cart_id: str

    class Config:
        orm_mode = True
