from fastapi import HTTPException, Response
from app.products.services import ReelServices, ProductTypeServices
from app.products.exceptions import *


class ReelController:

    @staticmethod
    def create_new_reel(brand: str, model: str, weight: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
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
        reel = ReelServices.get_reel_by_id(reel_id=reel_id)
        if reel:
            return reel
        raise HTTPException(status_code=400, detail=f"Reel with provided ID: {reel_id} is not exist")

    @staticmethod
    def get_reel_by_brand_name(brand: str):
        reel = ReelServices.get_reels_by_brand_name(brand=brand)
        if reel:
            return reel
        raise HTTPException(status_code=400, detail=f"Reels from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_reels():
        reels = ReelServices.get_all_reels()
        return reels

    @staticmethod
    def delete_reel_by_id(reel_id: str):
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
        try:
            return ReelServices.update_reel(reel_id=reel_id, brand=brand, model=model, weight=weight, AFTM=AFTM,
                                            price=price, quantity=quantity, description=description, in_stock=in_stock,
                                            product_id=product_id, product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
