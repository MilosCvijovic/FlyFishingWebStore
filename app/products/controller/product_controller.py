from sqlalchemy.exc import IntegrityError

from app.products.exceptions import ProductNotFoundException
from app.products.services.product_service import ProductServices
from app.users.services import UserServices, signJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidPassword


class ProductController:
    """Controller class for Product operations."""

    @staticmethod
    def create_product(name: str, price: float, quantity: int, description: str):

        try:
            product = ProductServices.create_product(name=name, price=price, quantity=quantity, description=description)
            return product
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Product with provided name: {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_product_by_id(product_id: str):
        product = ProductServices.get_product_by_id(product_id)
        if product:
            return product
        raise HTTPException(status_code=400, detail=f"Product with provided id {product_id} does not exist")

    @staticmethod
    def get_all_product():
        product = ProductServices.get_all_products()
        return product

    @staticmethod
    def update_product(product_id: str, name: str, price: float, quantity: int, description: str):
        try:
            product = ProductServices.update_product(product_id=product_id, name=name, price=price,
                                                     quantity=quantity, description=description)
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_product_by_id(product_id: str):
        try:
            ProductServices.delete_product_by_id(product_id)
            return Response(content=f"Product with provided ID: {product_id} is deleted")
        except ProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
