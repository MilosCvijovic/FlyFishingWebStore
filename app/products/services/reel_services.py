from app.db.database import SessionLocal
from app.products.repositories import ReelRepository


class ReelServices:
    @staticmethod
    def create_new_reel(brand: str, model: str, weight: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.create_new_reel(brand=brand, model=model, weight=weight,
                                                       AFTM=AFTM, price=price, quantity=quantity,
                                                       description=description, in_stock=in_stock,
                                                       product_id=product_id, product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_reel_by_id(reel_id: str):
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.get_reel_by_id(reel_id=reel_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_reels_by_brand_name(brand: str):
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.get_reels_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_reels():
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.get_all_reels()
        except Exception as e:
            raise e

    @staticmethod
    def delete_reel_by_id(reel_id: str):
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                reel_repository.delete_reel_by_id(reel_id=reel_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_reel(reel_id: str, brand: str = None, model: str = None, weight: int = None, AFTM: str = None,
                    price: int = None, quantity: int = None, description: str = None, in_stock: bool = None,
                    product_id: str = None, product_type_id: str = None):
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.update_reel(reel_id=reel_id, brand=brand, model=model, weight=weight, AFTM=AFTM,
                                                   price=price, quantity=quantity, description=description,
                                                   product_id = product_id, in_stock=in_stock,
                                                   product_type_id=product_type_id)
        except Exception as e:
            raise e
