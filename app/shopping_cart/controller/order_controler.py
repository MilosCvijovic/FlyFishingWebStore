from fastapi import HTTPException, Response
from app.shopping_cart.exceptions import *
from app.shopping_cart.services import OrderServices


class OrderController:

    @staticmethod
    def create_new_order(shopping_cart_id: str):
        try:
            order = OrderServices.create_new_order(shopping_cart_id=shopping_cart_id)
            return order
        except OrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_order_by_id(order_id: str):
        order = OrderServices.get_order_by_id(order_id=order_id)
        if order:
            return order
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {order_id} is not exist")

    @staticmethod
    def get_all_orders():
        order = OrderServices.get_all_orders()
        return order

    @staticmethod
    def delete_order_by_id(order_id: str):
        try:
            OrderServices.delete_order_by_id(order_id=order_id)
            return Response(content=f"Rod with provided ID: {order_id} is not exist")
        except OrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def mark_order_as_sent(order_id: str, shopping_cart_id: str, sent: bool):
        try:
            return OrderServices.mark_as_sent(order_id=order_id, shopping_cart_id=shopping_cart_id, sent=sent)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
