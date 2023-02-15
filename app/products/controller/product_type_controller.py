from sqlalchemy.exc import IntegrityError

from app.products.exceptions import ProductTypeNotFoundException
from app.products.services.product_type_service import ProductTypeServices
from app.users.services import UserServices, signJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidPassword


class ProductTypeController:
    """Controller class for Product operations."""

    @staticmethod
    def create_product_type(product_type: str):

        try:
            product = ProductTypeServices.create_product_type(product_type=product_type)
            return product
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Product with provided name: {product_type} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_product_type_by_id(product_id: str):
        product = ProductTypeServices.get_product_type_by_id(product_id)
        if product:
            return product
        raise HTTPException(status_code=400, detail=f"Product with provided id {product_id} does not exist")

    @staticmethod
    def get_all_product_types():
        product = ProductTypeServices.get_all_product_types()
        return product

    @staticmethod
    def update_product_type(product_type_id: str, product_type: str):
        try:
            product = ProductTypeServices.update_product_type(product_type_id=product_type_id,
                                                              product_type=product_type)
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_product_type_by_id(product_type_id: str):
        try:
            ProductTypeServices.delete_product_type_by_id(product_type_id)
            return Response(content=f"Product with provided ID: {product_type_id} is deleted")
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
