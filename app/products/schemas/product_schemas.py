from pydantic import BaseModel
from pydantic import UUID4


class ProductSchema(BaseModel):
    product_id: UUID4
    brand: str
    model: str
    price: int

    class Config:
        orm_mode = True


class ProductSchemaIn(BaseModel):
    brand: str
    model: str
    price: int

    class Config:
        orm_mode = True
