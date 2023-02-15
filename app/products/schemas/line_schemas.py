from typing import Optional

from pydantic import BaseModel
from pydantic import UUID4


class LineSchema(BaseModel):
    line_id: UUID4
    brand: str
    model: str
    length: int
    AFTM: str
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool
    product_type_id: str

    class Config:
        orm_mode = True


class LineSchemaIn(BaseModel):
    product_type_id: str
    brand: str
    model: str
    length: int
    AFTM: str
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool

    class Config:
        orm_mode = True
