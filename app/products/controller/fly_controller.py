from fastapi import HTTPException, Response
from app.products.services import FlyServices, ProductTypeServices
from app.products.exceptions import *


class FlyController:
    @staticmethod
    def create_new_fly(brand: str, model: str, length: int, weight: int, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Create a new Fly product.

            :param brand: The brand of the Fly.
            :param model: The model of the Fly.
            :param length: The length of the Fly in inches.
            :param weight: The weight of the Fly in ounces.
            :param price: The price of the Fly in USD.
            :param quantity: The quantity of the Fly in stock.
            :param description: The description of the Fly.
            :param in_stock: Whether the Fly is in stock or not.
            :param product_id: The ID of the product.
            :param product_type_id: The ID of the product type.
            :return: The created Fly product.
            :raises: HTTPException if the product type ID is not found or if there is an internal server error.
            """
        try:
            ProductTypeServices.get_product_type_by_id(product_type_id=product_type_id)
            fly = FlyServices.create_new_fly(brand=brand, model=model, length=length, weight=weight,
                                             price=price, quantity=quantity,
                                             description=description, in_stock=in_stock, product_id=product_id,
                                             product_type_id=product_type_id)
            return fly
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_fly_by_id(fly_id: str):
        """
           Get a Fly product by its ID.

           :param fly_id: The ID of the Fly product.
           :return: The Fly product.
           :raises: HTTPException if the Fly product does not exist.
           """
        fly = FlyServices.get_fly_by_id(fly_id=fly_id)
        if fly:
            return fly
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {fly_id} is not exist")

    @staticmethod
    def get_fly_by_brand_name(brand: str):
        """
            Get a list of Fly products by brand name.

            :param brand: The name of the Fly brand.
            :return: A list of Fly products.
            :raises: HTTPException if no Fly products are found for the provided brand.

            """
        fly = FlyServices.get_flies_by_brand_name(brand=brand)
        if fly:
            return fly
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_flies():
        """
            Get all Fly products.

            :return: A list of all Fly products.
            """
        fly = FlyServices.get_all_flies()
        return fly

    @staticmethod
    def delete_fly_by_id(fly_id: str):
        """
            Delete a Fly product by its ID.

            :param fly_id: The ID of the Fly product.
            :return: A response indicating that the Fly product has been deleted.
            :raises: HTTPException if the Fly product does not exist or if there is an internal server error.
            """
        try:
            FlyServices.delete_fly_by_id(fly_id=fly_id)
            return Response(content=f"Fly with provided ID: {fly_id} is not exist")
        except FlyNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_fly(fly_id: str, brand: str = None, model: str = None, length: int = None,
                   weight: int = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
        """
            Update a Fly product by its ID.

            :param fly_id: The ID of the Fly product.
            :param brand: The updated brand of the Fly product.
            :param model: The updated model of the Fly product.
            :param length: The updated length of the Fly product in inches.
            :param weight: The updated weight of the Fly product in ounces.
            :param price: The updated price of the Fly product in USD.
            :param quantity: The updated quantity of the Fly product in stock.
            :param description: The updated description of the Fly product.
            :param in_stock: Whether the Fly product is in stock or not.
            :param product_id: The updated ID of the product.
            :param product_type_id: The updated ID of the product type.
            :return: The updated Fly product.
            :raises: HTTPException if there is an internal server error.
            """
        try:
            return FlyServices.update_fly(fly_id=fly_id, brand=brand, model=model, length=length,
                                          weight=weight, price=price, quantity=quantity,
                                          description=description, in_stock=in_stock, product_id=product_id,
                                          product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
