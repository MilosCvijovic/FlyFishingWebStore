from fastapi import HTTPException, Response
from app.products.services import RodServices, ProductTypeServices
from app.products.exceptions import *


class RodController:
    """
       Controller class for handling HTTP requests related to rods.
       """
    @staticmethod
    def create_new_rod(brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Create a new rod with the given parameters.

            :param brand: str, the brand of the rod.
            :param model: str, the model of the rod.
            :param length: int, the length of the rod.
            :param weight: int, the weight of the rod.
            :param AFTM: str, the AFTM rating of the rod.
            :param price: int, the price of the rod.
            :param quantity: int, the quantity of the rod.
            :param description: str, the description of the rod.
            :param in_stock: bool, whether the rod is in stock or not.
            :param product_id: str, the id of the product the rod belongs to.
            :param product_type_id: str, the id of the product type the rod belongs to.
            :return: dict, the created rod.
            :raises: HTTPException with status_code 404 if the product type with the provided id does not exist.
                     HTTPException with status_code 500 for any other error.
            """
        try:
            ProductTypeServices.get_product_type_by_id(product_type_id=product_type_id)
            rod = RodServices.create_new_rod(brand=brand, model=model, length=length, weight=weight,
                                             AFTM=AFTM, price=price, quantity=quantity,
                                             description=description, in_stock=in_stock, product_id=product_id,
                                             product_type_id=product_type_id)
            return rod
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_rod_by_id(rod_id: str):
        """
            Get the rod with the given id.

            :param rod_id: str, the id of the rod to get.
            :return: dict, the rod with the given id.
            :raises: HTTPException with status_code 400 if a rod with the provided id does not exist.
            """
        rod = RodServices.get_rod_by_id(rod_id=rod_id)
        if rod:
            return rod
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {rod_id} is not exist")

    @staticmethod
    def get_rod_by_brand_name(brand: str):
        """
            Get all rods from the provided brand.

            :param brand: str, the brand to get the rods from.
            :return: dict, all rods from the provided brand.
            :raises: HTTPException with status_code 400 if no rods were found for the provided brand.
            """
        rod = RodServices.get_rods_by_brand_name(brand=brand)
        if rod:
            return rod
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_rods():
        """
            Get all rods.

           :return: dict, all rods.
           """
        rods = RodServices.get_all_rods()
        return rods

    @staticmethod
    def delete_rod_by_id(rod_id: str):
        """
           Delete the rod with the given id.

           :param rod_id: str, the id of the rod to delete.
           :return: Response with content indicating the rod has been deleted.
           :raises: HTTPException with status_code 400 if a rod with the provided id does not exist.
                    HTTPException with status_code 500 for any other error.
           """
        try:
            RodServices.delete_rod_by_id(rod_id=rod_id)
            return Response(content=f"Rod with provided ID: {rod_id} is not exist")
        except RodNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_rod(rod_id: str, brand: str = None, model: str = None, length: int = None,
                   weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
        """
                Updates an existing rod with the specified attributes. At least one attribute must be provided.

                :param rod_id: str, the id of the rod to be updated.
                :param brand: str, the new brand of the rod (optional).
                :param model: str, the new model of the rod (optional).
                :param length: int, the new length of the rod in feet (optional).
                :param weight: int, the new weight of the rod in grams (optional).
                :param AFTM: str, the new AFTM rating of the rod (optional).
                :param price: int, the new price of the rod in cents (optional).
                :param quantity: int, the new quantity of the rod in stock (optional).
                :param description: str, the new description of the rod (optional).
                :param in_stock: bool, the new availability status of the rod (optional).
                :param product_id: str, the new id of the product this rod belongs to (optional).
                :param product_type_id: str, the new id of the product type this rod belongs to (optional).
                :return: dict, the updated rod.
                :raises: HTTPException with status_code 400 if no attributes are provided.
                         HTTPException with status_code 400 if the rod with the provided id does not exist.
                         HTTPException with status_code 500 for any other error.
                """
        try:
            return RodServices.update_rod(rod_id=rod_id, brand=brand, model=model, length=length,
                                          weight=weight, AFTM=AFTM, price=price, quantity=quantity,
                                          description=description, in_stock=in_stock, product_id=product_id,
                                          product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
