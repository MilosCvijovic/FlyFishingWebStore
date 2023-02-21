from typing import Optional

from pydantic import BaseModel
from pydantic import UUID4


class FlySchema(BaseModel):
    fly_id: UUID4
    product_id: str
    brand: str
    model: str
    length: int
    weight: int
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool
    product_type_id: str

    class Config:
        orm_mode = True


class FlySchemaIn(BaseModel):
    product_type_id: str
    product_id: str
    brand: str
    model: str
    length: int
    weight: int
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool

    class Config:
        orm_mode = True
