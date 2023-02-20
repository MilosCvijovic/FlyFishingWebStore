from app.db.database import SessionLocal
from app.products.repositories import RodRepository


class RodServices:
    @staticmethod
    def create_new_rod(brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.create_new_rod(brand=brand, model=model, length=length, weight=weight,
                                                     AFTM=AFTM, price=price, quantity=quantity,
                                                     description=description, in_stock=in_stock, product_id=product_id,
                                                     product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_rod_by_id(rod_id: str):
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.get_rod_by_id(rod_id=rod_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_rods_by_brand_name(brand: str):
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.get_rods_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_rods():
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.get_all_rods()
        except Exception as e:
            raise e

    @staticmethod
    def delete_rod_by_id(rod_id: str):
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                rod_repository.delete_rod_by_id(rod_id=rod_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_rod(rod_id: str, brand: str = None, model: str = None, length: int = None,
                   weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.update_rod(rod_id=rod_id, brand=brand, model=model, length=length,
                                                 weight=weight, AFTM=AFTM, price=price, quantity=quantity,
                                                 description=description, in_stock=in_stock, product_id=product_id,
                                                 product_type_id=product_type_id)
        except Exception as e:
            raise e
