from fastapi import HTTPException, Response
from app.products.services import LineServices, ProductTypeServices
from app.products.exceptions import *


class LineController:

    @staticmethod
    def create_new_line(brand: str, model: str, length: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Create a new Line product.

            :param brand: The brand of the Line.
            :param model: The model of the Line.
            :param length: The length of the Line in feet.
            :param AFTM: The line weight class in AFTM rating system.
            :param price: The price of the Line in USD.
            :param quantity: The quantity of the Line in stock.
            :param description: The description of the Line.
            :param in_stock: Whether the Line is in stock or not.
            :param product_id: The ID of the product.
            :param product_type_id: The ID of the product type.
            :return: The created Line product.
            :raises: HTTPException if the product type ID is not found or if there is an internal server error.
            """
        try:
            ProductTypeServices.get_product_type_by_id(product_type_id=product_type_id)
            line = LineServices.create_new_line(brand=brand, model=model, length=length,
                                             AFTM=AFTM, price=price, quantity=quantity,
                                             description=description, in_stock=in_stock, product_id=product_id,
                                             product_type_id=product_type_id)
            return line
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_line_by_id(line_id: str):
        """
            Get a Line product by its ID.

            :param line_id: The ID of the Line product.
            :return: The Line product.
            :raises: HTTPException if the Line product does not exist.
            """
        line = LineServices.get_line_by_id(line_id=line_id)
        if line:
            return line
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {line_id} is not exist")

    @staticmethod
    def get_line_by_brand_name(brand: str):
        """
            Get a list of Line products by brand name.

            :param brand: The name of the Line brand.
            :return: A list of Line products.
            :raises: HTTPException if no Line products are found for the provided brand.
            """
        line = LineServices.get_lines_by_brand_name(brand=brand)
        if line:
            return line
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_lines():
        """
            Get all Line products.

            :return: A list of all Line products.
            """
        lines = LineServices.get_all_lines()
        return lines

    @staticmethod
    def delete_line_by_id(line_id: str):
        """
            Delete a Line product by its ID.

            :param line_id: The ID of the Line product.
            :return: A response indicating that the Line product has been deleted.
            :raises: HTTPException if the Line product does not exist or if there is an internal server error.
            """
        try:
            LineServices.delete_line_by_id(line_id=line_id)
            return Response(content=f"Rod with provided ID: {line_id} is not exist")
        except LineNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_line(line_id: str, brand: str = None, model: str = None, length: int = None,
                    AFTM: str = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
        """
            Update a Line product by its ID.

            :param line_id: The ID of the Line product.
            :param brand: The brand of the Line product.
            :param model: The model of the Line product.
            :param length: The length of the Line product in feet.
            :param AFTM: The line weight class in AFTM rating system.
            :param price: The price of the Line product in USD.
            :param quantity: The quantity of the Line product in stock.
            :param description: The description of the Line product.
            :param in_stock: Whether the Line product is in stock or not.
            :param product_id: The ID of the product.
            :param product_type_id: The ID of the product type.
            :return: The updated Line product.
            :raises: HTTPException if the Line product does not exist or if there is an internal server error.
            """
        try:
            return LineServices.update_line(line_id=line_id, brand=brand, model=model, length=length,
                                          AFTM=AFTM, price=price, quantity=quantity,
                                          description=description, in_stock=in_stock, product_id=product_id,
                                          product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
