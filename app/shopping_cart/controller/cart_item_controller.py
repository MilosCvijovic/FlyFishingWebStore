from fastapi import HTTPException, Response
from app.shopping_cart.exceptions import *
from app.shopping_cart.services import CartItemServices


class CartItemController:
    """
       Controller class for managing cart items.
       """

    @staticmethod
    def create_new_cart_item(quantity: int, product_id: str, shopping_cart_id: str):
        """
           :param quantity: The quantity of the product to add to the cart.
           :param product_id: The ID of the product to add to the cart.
           :param shopping_cart_id: The ID of the shopping cart to add the product to.
           :return: CartItem: The created cart item.
           :raises: HTTPException: If the specified cart item cannot be created.
           """
        try:
            cart_item = CartItemServices.create_new_cart_item(quantity=quantity, product_id=product_id,
                                                              shopping_cart_id=shopping_cart_id)
            return cart_item
        except CartItemNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_cart_item_by_id(cart_id: str):
        """
            :param cart_id: The ID of the cart item to retrieve.
            :return: CartItem: The cart item with the specified ID.
            :raises: HTTPException: If the specified cart item does not exist.
            """
        cart_item = CartItemServices.get_cart_item_by_id(cart_id=cart_id)
        if cart_item:
            return cart_item
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {cart_id} is not exist")

    @staticmethod
    def get_all_cart_items():
        """
            :return: List of all cart items.
            """
        cart_item = CartItemServices.get_all_cart_items()
        return cart_item

    @staticmethod
    def delete_cart_item_by_id(cart_id: str):
        """
            :param cart_id: The ID of the cart item to delete.
            :return: Response: A response indicating the success or failure of the operation.
            :raises: HTTPException: If the specified cart item does not exist.
            """
        try:
            CartItemServices.delete_cart_item_by_id(cart_id=cart_id)
            return Response(content=f"Rod with provided ID: {cart_id} is not exist")
        except CartItemNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_cart_item(cart_id: str, product_id: str, quantity: int = None):
        """
            :param cart_id: The ID of the cart item to update.
            :param product_id: The new ID of the product for the cart item.
            :param quantity: The new quantity for the cart item (optional).
            :return: CartItem: The updated cart item.
            :raises: HTTPException: If the specified cart item cannot be updated.
            """
        try:
            return CartItemServices.update_cart_item(cart_id=cart_id, product_id=product_id, quantity=quantity)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
