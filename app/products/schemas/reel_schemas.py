from typing import Optional

from pydantic import BaseModel
from pydantic import UUID4


class ReelSchema(BaseModel):
    """
       Schema representing a reel product with all its details.

       :param reel_id: The UUID4 id of the reel.
       :param product_id: The id of the product.
       :param brand: The brand name of the reel.
       :param model: The model name of the reel.
       :param weight: The weight of the reel (optional).
       :param AFTM: The AFTM number of the reel.
       :param price: The price of the reel.
       :param quantity: The quantity of the reel in stock.
       :param description: The description of the reel (optional).
       :param in_stock: Whether the reel is currently in stock.
       :param product_type_id: The id of the product type this reel belongs to.

       :return: A `ReelSchema` instance representing a reel product.
       """
    reel_id: UUID4
    product_id: str
    brand: str
    model: str
    weight: Optional[int]
    AFTM: str
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool
    product_type_id: str

    class Config:
        orm_mode = True


class ReelSchemaIn(BaseModel):
    """
        Schema for inserting reel product into the database.

        :param product_type_id: The id of the product type this reel belongs to.
        :param product_id: The id of the product.
        :param brand: The brand name of the reel.
        :param model: The model name of the reel.
        :param weight: The weight of the reel (optional).
        :param AFTM: The AFTM number of the reel.
        :param price: The price of the reel.
        :param quantity: The quantity of the reel in stock.
        :param description: The description of the reel (optional).
        :param in_stock: Whether the reel is currently in stock.
        """
    product_type_id: str
    product_id: str
    brand: str
    model: str
    weight: Optional[int]
    AFTM: str
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool

    class Config:
        orm_mode = True
