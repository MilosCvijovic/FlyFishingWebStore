from fastapi import HTTPException, Response
from app.products.services import ReelServices, ProductTypeServices
from app.products.exceptions import *


class ReelController:
    """Controller class for Reel operations."""
    @staticmethod
    def create_new_reel(brand: str, model: str, weight: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Create a new reel with the provided details.

            :param brand: The brand of the reel.
            :param model: The model of the reel.
            :param weight: The weight of the reel.
            :param AFTM: The AFTM of the reel.
            :param price: The price of the reel.
            :param quantity: The quantity of the reel.
            :param description: The description of the reel.
            :param in_stock: Whether the reel is in stock or not.
            :param product_id: The id of the product the reel belongs to.
            :param product_type_id: The id of the product type the reel belongs to.
            :return: The newly created reel.
            :raises: HTTPException with status_code 400 if a product type with the provided id does not exist.
                     HTTPException with status_code 500 for any other error.
            """

        try:
            ProductTypeServices.get_product_type_by_id(product_type_id=product_type_id)
            reel = ReelServices.create_new_reel(brand=brand, model=model, weight=weight,
                                                AFTM=AFTM, price=price, quantity=quantity,
                                                description=description, in_stock=in_stock, product_id=product_id,
                                                product_type_id=product_type_id)
            return reel
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_reel_by_id(reel_id: str):
        """
            Retrieve a reel with the provided id.

            :param reel_id: The id of the reel.
            :return: The reel with the provided id.
            :raises: HTTPException with status_code 400 if a reel with the provided id does not exist.
            """
        reel = ReelServices.get_reel_by_id(reel_id=reel_id)
        if reel:
            return reel
        raise HTTPException(status_code=400, detail=f"Reel with provided ID: {reel_id} is not exist")

    @staticmethod
    def get_reel_by_brand_name(brand: str):
        """
           Retrieve all reels from the manufacturer with the provided name.

           :param brand: The name of the manufacturer.
           :return: A list of reels from the manufacturer.
           :raises: HTTPException with status_code 400 if no reels from the manufacturer are found.
           """
        reel = ReelServices.get_reels_by_brand_name(brand=brand)
        if reel:
            return reel
        raise HTTPException(status_code=400, detail=f"Reels from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_reels():
        """
            Retrieve all reels.

            :return: A list of all reels.
            """
        reels = ReelServices.get_all_reels()
        return reels

    @staticmethod
    def delete_reel_by_id(reel_id: str):
        """
            Delete the reel with the provided id.

            :param reel_id: The id of the reel to be deleted.
            :return: Response with content indicating the reel has been deleted.
            :raises: HTTPException with status_code 400 if a reel with the provided id does not exist.
                     HTTPException with status_code 500 for any other error.
            """
        try:
            ReelServices.delete_reel_by_id(reel_id=reel_id)
            return Response(content=f"Reel with provided ID: {reel_id} is not exist")
        except ReelNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_reel(reel_id: str, brand: str = None, model: str = None, weight: int = None, AFTM: str = None,
                    price: int = None, quantity: int = None, description: str = None, in_stock: bool = None,
                    product_id: str = None, product_type_id: str = None):
        """Update an existing reel by providing its ID and the fields to update.

        :param reel_id: str, the ID of the reel to be updated.
        :param brand: str, the new brand name for the reel (optional).
        :param model: str, the new model name for the reel (optional).
        :param weight: int, the new weight for the reel (optional).
        :param AFTM: str, the new AFTM value for the reel (optional).
        :param price: int, the new price for the reel (optional).
        :param quantity: int, the new quantity for the reel (optional).
        :param description: str, the new description for the reel (optional).
        :param in_stock: bool, whether the reel is in stock or not (optional).
        :param product_id: str, the new product ID associated with the reel (optional).
        :param product_type_id: str, the new product type ID associated with the reel (optional).
        :return: dict, a dictionary representing the updated reel object.
        :raises: HTTPException with status_code 500 for any errors during the update process."""
        try:
            return ReelServices.update_reel(reel_id=reel_id, brand=brand, model=model, weight=weight, AFTM=AFTM,
                                            price=price, quantity=quantity, description=description, in_stock=in_stock,
                                            product_id=product_id, product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
