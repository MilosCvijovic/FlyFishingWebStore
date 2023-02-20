from app.config import settings
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword

from app.products.repositories import ProductTypeRepository


class ProductTypeServices:

    @staticmethod
    def create_product_type(product_type: str, ):
        with SessionLocal() as db:
            try:
                product_repository = ProductTypeRepository(db)
                return product_repository.create_product_type(product_type=product_type)
            except Exception as e:
                raise e

    @staticmethod
    def get_product_type_by_id(product_type_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.get_product_type_by_id(product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_product_types():
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.get_all_product_types()
        except Exception as e:
            raise e

    @staticmethod
    def update_product_type(product_type_id: str, product_type: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.update_product_type(product_type_id=product_type_id,
                                                              product_type=product_type)
        except Exception as e:
            raise e

    @staticmethod
    def delete_product_type_by_id(product_type_id):
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.delete_product_type_by_id(product_type_id)
        except Exception as e:
            raise e
