from fastapi import HTTPException, Response
from app.shopping_cart.exceptions import *
from app.shopping_cart.services import CartItemServices


class CartItemController:

    @staticmethod
    def create_new_cart_item(quantity: int, product_id: str, shopping_cart_id: str):
        try:
            cart_item = CartItemServices.create_new_cart_item(quantity=quantity, product_id=product_id, shopping_cart_id=shopping_cart_id)
            return cart_item
        except CartItemNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_cart_item_by_id(cart_id: str):
        cart_item = CartItemServices.get_cart_item_by_id(cart_id=cart_id)
        if cart_item:
            return cart_item
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {cart_id} is not exist")

    @staticmethod
    def get_all_cart_items():
        cart_item = CartItemServices.get_all_cart_items()
        return cart_item

    @staticmethod
    def delete_cart_item_by_id(cart_id: str):
        try:
            CartItemServices.delete_cart_item_by_id(cart_id=cart_id)
            return Response(content=f"Rod with provided ID: {cart_id} is not exist")
        except CartItemNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_cart_item(cart_id: str, product_id: str, quantity: int = None):
        try:
            return CartItemServices.update_cart_item(cart_id=cart_id, product_id=product_id, quantity=quantity)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
