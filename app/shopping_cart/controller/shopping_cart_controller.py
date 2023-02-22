from fastapi import HTTPException, Response
from app.shopping_cart.exceptions import *
from app.shopping_cart.services import ShoppingCartServices


class ShoppingCartController:

    @staticmethod
    def create_new_shopping_cart(customer_id: str):
        """
            Creates a new shopping cart for the provided customer.

            :param customer_id: The ID of the customer for whom the shopping cart is being created.
            :return: A dictionary representing the created shopping cart.
            :raises HTTPException: If there is a server error or if the provided customer ID is not valid.
            """
        try:
            shopping_cart = ShoppingCartServices.create_shopping_cart(customer_id=customer_id)
            return shopping_cart
        except ShoppingCartNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_shopping_cart_by_id(shopping_cart_id: str):
        """
            Retrieves the shopping cart with the provided ID.

            :param shopping_cart_id: The ID of the shopping cart to retrieve.
            :return: A dictionary representing the retrieved shopping cart.
            :raises HTTPException: If there is a server error or if the shopping cart with the
            provided ID does not exist.
            """
        shopping_cart = ShoppingCartServices.get_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
        if shopping_cart:
            return shopping_cart
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {shopping_cart_id} is not exist")

    @staticmethod
    def get_all_shopping_carts():
        """
            Retrieves all shopping carts.

            :return: A list of dictionaries representing all shopping carts.
            """
        shopping_cart = ShoppingCartServices.get_all_shopping_carts()
        return shopping_cart

    @staticmethod
    def delete_shopping_cart_by_id(shopping_cart_id: str):
        """
            Deletes the shopping cart with the provided ID.

            :param shopping_cart_id: The ID of the shopping cart to delete.
            :return: A response indicating the result of the deletion.
            :raises HTTPException: If there is a server error or if the shopping cart with the
            provided ID does not exist.
            """
        try:
            ShoppingCartServices.delete_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
            return Response(content=f"Rod with provided ID: {shopping_cart_id} is not exist")
        except ShoppingCartNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_shopping_cart(shopping_cart_id: str, customer_id: str = None):
        """
            Updates the shopping cart with the provided ID.

            :param shopping_cart_id: The ID of the shopping cart to update.
            :param customer_id: The new customer ID to associate with the shopping cart. If not provided,
            the customer ID will not be updated.
            :return: A dictionary representing the updated shopping cart.
            :raises HTTPException: If there is a server error or if the shopping cart with the
            provided ID does not exist.
            """
        try:
            return ShoppingCartServices.update_shopping_cart(shopping_cart_id=shopping_cart_id, customer_id=customer_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
