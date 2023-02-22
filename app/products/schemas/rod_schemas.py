from typing import Optional

from pydantic import BaseModel
from pydantic import UUID4


class RodSchema(BaseModel):
    """
       Represents a rod schema.

       :param rod_id: The unique ID of the rod.
       :param product_id: The ID of the product associated with the rod.
       :param brand: The brand of the rod.
       :param model: The model of the rod.
       :param length: The length of the rod.
       :param weight: The weight of the rod.
       :param AFTM: The AFTM rating of the rod.
       :param price: The price of the rod.
       :param quantity: The quantity of the rod.
       :param description: The description of the rod.
       :param in_stock: Whether the rod is in stock or not.
       :param product_type_id: The ID of the product type associated with the rod.
       """
    rod_id: UUID4
    product_id: str
    brand: str
    model: str
    length: int
    weight: Optional[int]
    AFTM: str
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool
    product_type_id: str

    class Config:
        orm_mode = True


class RodSchemaIn(BaseModel):
    """
        Represents an input rod schema.

        :param product_type_id: The ID of the product type associated with the rod.
        :param product_id: The ID of the product associated with the rod.
        :param brand: The brand of the rod.
        :param model: The model of the rod.
        :param length: The length of the rod.
        :param weight: The weight of the rod.
        :param AFTM: The AFTM rating of the rod.
        :param price: The price of the rod.
        :param quantity: The quantity of the rod.
        :param description: The description of the rod.
        :param in_stock: Whether the rod is in stock or not.
        """
    product_type_id: str
    product_id: str
    brand: str
    model: str
    length: int
    weight: Optional[int]
    AFTM: str
    price: int
    quantity: int
    description: Optional[str]
    in_stock: bool

    class Config:
        orm_mode = True
