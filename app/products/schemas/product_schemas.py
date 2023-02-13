from pydantic import BaseModel
from pydantic import UUID4


class ProductSchema(BaseModel):
    product_id: UUID4
    name: str
    price: float
    quantity: int
    description: str

    class Config:
        orm_mode = True


class ProductSchemaIn(BaseModel):
    name: str
    price: float
    quantity: int
    description: str

    class Config:
        orm_mode = True
