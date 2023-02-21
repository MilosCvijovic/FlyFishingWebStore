from fastapi import HTTPException, Response
from app.products.services import FlyServices, ProductTypeServices
from app.products.exceptions import *


class FlyController:

    @staticmethod
    def create_new_fly(brand: str, model: str, length: int, weight: int, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
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
        fly = FlyServices.get_fly_by_id(fly_id=fly_id)
        if fly:
            return fly
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {fly_id} is not exist")

    @staticmethod
    def get_fly_by_brand_name(brand: str):
        fly = FlyServices.get_flies_by_brand_name(brand=brand)
        if fly:
            return fly
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_flies():
        fly = FlyServices.get_all_flies()
        return fly

    @staticmethod
    def delete_fly_by_id(fly_id: str):
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
        try:
            return FlyServices.update_fly(fly_id=fly_id, brand=brand, model=model, length=length,
                                          weight=weight, price=price, quantity=quantity,
                                          description=description, in_stock=in_stock, product_id=product_id,
                                          product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
