from fastapi import HTTPException, Response
from app.shopping_cart.exceptions import *
from app.shopping_cart.services import OrderServices


class OrderController:

    @staticmethod
    def create_new_order(shopping_cart_id: str):
        """
            :param shopping_cart_id: The id of the shopping cart associated with the order.
            :return: A dictionary representing the newly created order.
            :raises HTTPException: If the order is not found or if there is a server error.
            """
        try:
            order = OrderServices.create_new_order(shopping_cart_id=shopping_cart_id)
            return order
        except OrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_order_by_id(order_id: str):
        """
            :param order_id: The id of the order to retrieve.
            :return: A dictionary representing the order.
            :raises HTTPException: If the order with the provided ID does not exist.
            """
        order = OrderServices.get_order_by_id(order_id=order_id)
        if order:
            return order
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {order_id} is not exist")

    @staticmethod
    def get_all_orders():
        """
            :return: A list of all orders.
            """
        order = OrderServices.get_all_orders()
        return order

    @staticmethod
    def delete_order_by_id(order_id: str):
        """
            :param order_id: The id of the order to delete.
            :return: A Response object with a message indicating that the order was deleted.
            :raises HTTPException: If the order with the provided ID does not exist or if there is a server error.
            """
        try:
            OrderServices.delete_order_by_id(order_id=order_id)
            return Response(content=f"Rod with provided ID: {order_id} is not exist")
        except OrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def mark_order_as_sent(order_id: str, shopping_cart_id: str, sent: bool):
        """
            :param order_id: The id of the order to mark as sent.
            :param shopping_cart_id: The id of the shopping cart associated with the order.
            :param sent: A boolean value indicating whether the order has been sent.
            :return: A dictionary representing the updated order.
            :raises HTTPException: If the order with the provided ID does not exist or if there is a server error.
            """
        try:
            return OrderServices.mark_as_sent(order_id=order_id, shopping_cart_id=shopping_cart_id, sent=sent)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
