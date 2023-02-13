from app.config import settings
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword

from app.products.repositories import ProductRepository


class ProductServices:

    @staticmethod
    def create_product(name: str, price: float, quantity: int, description: str):
        with SessionLocal() as db:
            try:
                product_repository = ProductRepository(db)
                return product_repository.create_product(name=name, price=price,
                                                         quantity=quantity, description=description)
            except Exception as e:
                raise e

    @staticmethod
    def get_product_by_id(product_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.get_product_by_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_products():
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.get_all_products()
        except Exception as e:
            raise e

    @staticmethod
    def update_product(product_id: str, name: str, price: float, quantity: int, description: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.update_product(product_id=product_id, name=name, price=price,
                                                         quantity=quantity, description=description)
        except Exception as e:
            raise e

    @staticmethod
    def delete_product_by_id(product_id):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.delete_product_by_id(product_id)
        except Exception as e:
            raise e
