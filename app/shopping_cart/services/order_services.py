from app.db.database import SessionLocal
from app.shopping_cart.repository import OrderRepository, ShoppingCartRepository
from app.shopping_cart.schemas import ShoppingCartSchemaOut, CartItemSchema


class OrderServices:
    @staticmethod
    def create_new_order(shopping_cart_id: str):
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.create_new_order(shopping_cart_id=shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_order_by_id(order_id: str):
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.get_order_by_id(order_id=order_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_orders():
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.get_all_orders()
        except Exception as e:
            raise e

    @staticmethod
    def delete_order_by_id(order_id: str):
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                order_repository.delete_order_by_id(order_id=order_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def mark_as_sent(order_id: str, shopping_cart_id: str, sent: bool):
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.mark_order_as_sent(order_id=order_id, shopping_cart_id=shopping_cart_id, sent=sent)
        except Exception as e:
            raise e
