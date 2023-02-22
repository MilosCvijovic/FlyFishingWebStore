from app.db.database import SessionLocal
from app.shopping_cart.repository import OrderRepository


class OrderServices:
    @staticmethod
    def create_new_order(shopping_cart_id: str):
        """
            Create a new order with the given shopping cart id.

            :param shopping_cart_id: The id of the shopping cart.

            :return: None

            :raises Exception: If there was an error creating the order.
            """
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.create_new_order(shopping_cart_id=shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_order_by_id(order_id: str):
        """
           Retrieve an order by its id.

           :param order_id: The id of the order.

           :return: The order with the given id.

           :raises Exception: If there was an error retrieving the order.
           """
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.get_order_by_id(order_id=order_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_orders():
        """
            Retrieve all orders.

            :return: A list of all orders.

            :raises Exception: If there was an error retrieving the orders.
            """
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.get_all_orders()
        except Exception as e:
            raise e

    @staticmethod
    def delete_order_by_id(order_id: str):
        """
            Delete an order by its id.

            :param order_id: The id of the order.

            :return: True if the order was successfully deleted.

            :raises Exception: If there was an error deleting the order.
            """
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                order_repository.delete_order_by_id(order_id=order_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def mark_as_sent(order_id: str, shopping_cart_id: str, sent: bool):
        """
            Mark an order as sent.

            :param order_id: The id of the order.
            :param shopping_cart_id: The id of the shopping cart associated with the order.
            :param sent: True if the order has been sent, False otherwise.
            :raises Exception: If there was an error updating the order.
            """
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.mark_order_as_sent(order_id=order_id, shopping_cart_id=shopping_cart_id,
                                                           sent=sent)
        except Exception as e:
            raise e
