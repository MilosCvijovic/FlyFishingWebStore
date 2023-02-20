from pydantic import BaseModel
from pydantic import UUID4


class ProductTypeSchema(BaseModel):
    product_type_id: UUID4
    product_type: str

    class Config:
        orm_mode = True


class ProductTypeSchemaIn(BaseModel):
    product_type: str

    class Config:
        orm_mode = True
