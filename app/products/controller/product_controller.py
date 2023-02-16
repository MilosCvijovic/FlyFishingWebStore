from fastapi import HTTPException, Response
from app.products.services import ProductServices
from app.products.exceptions import *


class ProductController:

    @staticmethod
    def create_new_product(brand: str, model: str, price: int):
        try:
            product = ProductServices.create_new_product(brand=brand, model=model, price=price)
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_product_by_id(product_id: str):
        product = ProductServices.get_product_by_id(product_id=product_id)
        if product:
            return product
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {product_id} is not exist")

    @staticmethod
    def get_rod_by_brand_name(brand: str):
        products = ProductServices.get_products_by_brand_name(brand=brand)
        if products:
            return products
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_products():
        products = ProductServices.get_all_products()
        return products

    @staticmethod
    def delete_product_by_id(product_id: str):
        try:
            ProductServices.delete_product_by_id(product_id=product_id)
            return Response(content=f"Rod with provided ID: {product_id} is not exist")
        except ProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_product(product_id: str, brand: str = None, model: str = None, price: int = None):
        try:
            return ProductServices.update_product(product_id=product_id, brand=brand, model=model,price=price)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
