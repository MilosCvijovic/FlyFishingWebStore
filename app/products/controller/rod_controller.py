from fastapi import HTTPException, Response
from app.products.services import RodServices, ProductTypeServices
from app.products.exceptions import *


class RodController:

    @staticmethod
    def create_new_rod(brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_type_id: str):
        try:
            ProductTypeServices.get_product_type_by_id(product_type_id=product_type_id)
            rod = RodServices.create_new_rod(brand=brand, model=model, length=length, weight=weight,
                                             AFTM=AFTM, price=price, quantity=quantity,
                                             description=description, in_stock=in_stock,
                                             product_type_id=product_type_id)
            return rod
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_rod_by_id(rod_id: str):
        rod = RodServices.get_rod_by_id(rod_id=rod_id)
        if rod:
            return rod
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {rod_id} is not exist")

    @staticmethod
    def get_rod_by_brand_name(brand: str):
        rod = RodServices.get_rods_by_brand_name(brand=brand)
        if rod:
            return rod
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_rods():
        rods = RodServices.get_all_rods()
        return rods

    @staticmethod
    def delete_rod_by_id(rod_id: str):
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
                   description: str = None, in_stock: bool = None, product_type_id: str = None):
        try:
            return RodServices.update_rod(rod_id=rod_id, brand=brand, model=model, length=length,
                                          weight=weight, AFTM=AFTM, price=price, quantity=quantity,
                                          description=description, in_stock=in_stock,
                                          product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
