from app.db.database import SessionLocal
from app.shopping_cart.repository import CartItemRepository


class CartItemServices:
    @staticmethod
    def create_new_cart_item(quantity: int, product_id: str, shopping_cart_id: str):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.create_new_cart_item(quantity=quantity, product_id=product_id, shopping_cart_id=shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_cart_item_by_id(cart_id: str):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.get_cart_item_by_id(cart_id=cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_cart_items():
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.get_all_cart_items()
        except Exception as e:
            raise e

    @staticmethod
    def delete_cart_item_by_id(cart_id: str):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                cart_item_repository.delete_cart_item_by_id(cart_id=cart_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_cart_item(cart_id: str, product_id: str, quantity: int = None):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.update_cart_item(cart_id=cart_id, product_id=product_id, quantity=quantity)
        except Exception as e:
            raise e
