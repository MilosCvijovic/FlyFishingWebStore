from pydantic import BaseModel
from pydantic import UUID4


class ProductSchema(BaseModel):
    """
       Schema for creating product from the database.

       :param product_id: UUID4 identifying the product.
       :param brand: Brand of the product.
       :param model: Model of the product.
       :param price: Price of the product.

       :return: A ProductSchema instance representing a product from the database.
       """
    product_id: UUID4
    brand: str
    model: str
    price: int

    class Config:
        orm_mode = True


class ProductSchemaIn(BaseModel):
    """
        Schema for creating a new product.

        :param brand: Brand of the product.
        :param model: Model of the product.
        :param price: Price of the product.

        :return: A ProductSchemaIn instance representing a new product to be created in the database.
        """
    brand: str
    model: str
    price: int

    class Config:
        orm_mode = True
