from typing import Optional

from pydantic import BaseModel
from pydantic import UUID4


class LineSchema(BaseModel):
    """
        Schema for a fishing line product.

        :param line_id: The unique ID of the fishing line
        :param product_id: The unique ID of the product.
        :param brand: The brand of the fishing line.
        :param model: The model of the fishing line.
        :param length: The length of the fishing line in feet.
        :param AFTM: The weight class of the fishing line.
        :param price: The price of the fishing line in cents.
        :param quantity: The quantity of the fishing line in stock.
        :param description: An optional description of the fishing line.
        :param in_stock: Whether the fishing line is currently in stock.
        :param product_type_id: The unique ID of the product type.
        :return: A LineSchema object representing a fishing line product.
        """
    line_id: UUID4
    product_id: str
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
    """
        Schema for creating a fishing line product.

        :param product_id: The unique ID of the product.
        :param brand: The brand of the fishing line.
        :param model: The model of the fishing line.
        :param length: The length of the fishing line in feet.
        :param AFTM: The weight class of the fishing line.
        :param price: The price of the fishing line in cents.
        :param quantity: The quantity of the fishing line in stock.
        :param description: An optional description of the fishing line.
        :param in_stock: Whether the fishing line is currently in stock.
        :return: A LineSchemaIn object representing a fishing line product to be created.
        :raises ValueError: If any required field is missing or invalid.
        """
    product_type_id: str
    product_id: str
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
