from pydantic import BaseModel, UUID4


class OrderSchema(BaseModel):
    """Schema class for orders retrieved from the database."""
    order_id: UUID4
    shopping_cart_id: str
    sent: bool = False

    class Config:
        orm_mode = True


class OrderSchemaIn(BaseModel):
    """Schema class for incoming order data to be processed."""
    shopping_cart_id: str

    class Config:
        orm_mode = True


class OrderSchemaOut(BaseModel):
    """Schema class for outgoing order data returned to the client."""
    order_id: UUID4
    sent: bool = False

    class Config:
        orm_mode = True
