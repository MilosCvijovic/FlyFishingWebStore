from app.db.database import SessionLocal
from app.products.repositories import FlyRepository


class FlyServices:
    @staticmethod
    def create_new_fly(brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_type_id: str):
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.create_new_fly(brand=brand, model=model, length=length, weight=weight,
                                                     AFTM=AFTM, price=price, quantity=quantity,
                                                     description=description, in_stock=in_stock,
                                                     product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_fly_by_id(fly_id: str):
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.get_fly_by_id(fly_id=fly_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_flies_by_brand_name(brand: str):
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.get_flies_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_flies():
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.get_all_flies()
        except Exception as e:
            raise e

    @staticmethod
    def delete_fly_by_id(fly_id: str):
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                fly_repository.delete_fly_by_id(fly_id=fly_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_fly(fly_id: str, brand: str = None, model: str = None, length: int = None,
                   weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_type_id: str = None):
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.update_fly(fly_id=fly_id, brand=brand, model=model, length=length,
                                                 weight=weight, AFTM=AFTM, price=price, quantity=quantity,
                                                 description=description, in_stock=in_stock,
                                                 product_type_id=product_type_id)
        except Exception as e:
            raise e
