from pydantic import BaseModel
from pydantic import UUID4


class ProductTypeSchema(BaseModel):
    """
        Schema for creating product type.

        :param product_type_id: UUID of the product type.
        :param product_type: Name of the product type.
        :return: An instance of the ProductTypeSchema.
        """
    product_type_id: UUID4
    product_type: str

    class Config:
        orm_mode = True


class ProductTypeSchemaIn(BaseModel):
    """
        Schema representing a product type to be inserted into the database.

        :param product_type: Name of the product type.
        :return: An instance of the ProductTypeSchemaIn.

        """
    product_type: str

    class Config:
        orm_mode = True
