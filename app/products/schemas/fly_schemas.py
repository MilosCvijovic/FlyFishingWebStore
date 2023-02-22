from typing import Optional

from pydantic import BaseModel
from pydantic import UUID4


class FlySchema(BaseModel):
    """
        Schema representing a fly product.

        :param fly_id: UUID for the fly product.
        :param product_id: Unique identifier for the product.
        :param brand: Brand of the product.
        :param model: Model name of the product.
        :param length: Length of the product.
        :param weight: Weight of the product.
        :param price: Price of the product.
        :param quantity: Quantity of the product.
        :param description: Optional description of the product.
        :param in_stock: Boolean representing whether the product is in stock or not.
        :param product_type_id: Unique identifier for the type of product.
        """
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
    """
      Input schema representing a fly product.

      :param product_type_id: Unique identifier for the type of product.
      :param product_id: Unique identifier for the product.
      :param brand: Brand of the product.
      :param model: Model name of the product.
      :param length: Length of the product.
      :param weight: Weight of the product.
      :param price: Price of the product.
      :param quantity: Quantity of the product.
      :param description: Optional description of the product.
      :param in_stock: Boolean representing whether the product is in stock or not.
      """
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
