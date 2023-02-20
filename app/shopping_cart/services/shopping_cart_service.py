from app.db.database import SessionLocal
from app.shopping_cart.repository import ShoppingCartRepository


class ShoppingCartServices:
    @staticmethod
    def create_shopping_cart(customer_id: str):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.create_new_shopping_cart(customer_id=customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_shopping_cart_by_id(shopping_cart_id: str):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.get_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_shopping_carts():
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.get_all_shopping_carts()
        except Exception as e:
            raise e

    @staticmethod
    def delete_shopping_cart_by_id(shopping_cart_id: str):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_cart_repository.delete_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_shopping_cart(shopping_cart_id: str, customer_id: str = None):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.update_shopping_cart(shopping_cart_id=shopping_cart_id, customer_id=customer_id)
        except Exception as e:
            raise e
