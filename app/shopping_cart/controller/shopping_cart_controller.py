from fastapi import HTTPException, Response
from app.shopping_cart.exceptions import *
from app.shopping_cart.services import ShoppingCartServices


class ShoppingCartController:

    @staticmethod
    def create_new_shopping_cart(customer_id: str):
        try:
            shopping_cart = ShoppingCartServices.create_shopping_cart(customer_id=customer_id)
            return shopping_cart
        except ShoppingCartNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_shopping_cart_by_id(shopping_cart_id: str):
        shopping_cart = ShoppingCartServices.get_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
        if shopping_cart:
            return shopping_cart
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {shopping_cart_id} is not exist")

    @staticmethod
    def get_all_shopping_carts():
        shopping_cart = ShoppingCartServices.get_all_shopping_carts()
        return shopping_cart

    @staticmethod
    def delete_shopping_cart_by_id(shopping_cart_id: str):
        try:
            ShoppingCartServices.delete_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
            return Response(content=f"Rod with provided ID: {shopping_cart_id} is not exist")
        except ShoppingCartNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_shopping_cart(shopping_cart_id: str, customer_id: str = None):
        try:
            return ShoppingCartServices.update_shopping_cart(shopping_cart_id=shopping_cart_id, customer_id=customer_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
