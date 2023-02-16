from app.db.database import SessionLocal
from app.products.repositories import ProductRepository


class ProductServices:
    @staticmethod
    def create_new_product(brand: str, model: str, price: int):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.create_new_product(brand=brand, model=model, price=price)
        except Exception as e:
            raise e

    @staticmethod
    def get_product_by_id(product_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.get_product_by_id(product_id=product_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_products_by_brand_name(brand: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.get_products_by_brand_name(brand=brand)
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
    def delete_product_by_id(product_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                product_repository.delete_product_by_id(product_id=product_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_product(product_id: str, brand: str = None, model: str = None, price: int = None):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.update_product(product_id=product_id, brand=brand, model=model, price=price)
        except Exception as e:
            raise e
