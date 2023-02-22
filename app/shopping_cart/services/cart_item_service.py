from app.db.database import SessionLocal
from app.shopping_cart.repository import CartItemRepository


class CartItemServices:
    @staticmethod
    def create_new_cart_item(quantity: int, product_id: str, shopping_cart_id: str):
        """
            Create a new cart item with the given quantity, product_id and shopping_cart_id.

            :param quantity: The quantity of the product in the cart item.
            :param product_id: The id of the product.
            :param shopping_cart_id: The id of the shopping cart.

            :return: None

            :raises Exception: If there was an error creating the cart item.
            """
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.create_new_cart_item(quantity=quantity, product_id=product_id,
                                                                 shopping_cart_id=shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_cart_item_by_id(cart_id: str):
        """
            Retrieve a cart item by its id.

            :param cart_id: The id of the cart item.

            :return: The cart item with the given id.

            :raises Exception: If there was an error retrieving the cart item.
            """
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.get_cart_item_by_id(cart_id=cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_cart_items():
        """
            Retrieve all cart items.

            :return: A list of all cart items.

            :raises Exception: If there was an error retrieving the cart items.
            """
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.get_all_cart_items()
        except Exception as e:
            raise e

    @staticmethod
    def delete_cart_item_by_id(cart_id: str):
        """
            Delete a cart item by its id.

            :param cart_id: The id of the cart item.

            :return: True if the cart item was successfully deleted.

            :raises Exception: If there was an error deleting the cart item.
            """
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                cart_item_repository.delete_cart_item_by_id(cart_id=cart_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_cart_item(cart_id: str, product_id: str, quantity: int = None):
        """
            Update a cart item with the given id.

            :param cart_id: The id of the cart item to update.
            :param product_id: The id of the product.
            :param quantity: The quantity of the product in the cart item (optional).

            :return: None

            :raises Exception: If there was an error updating the cart item.
            """
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.update_cart_item(cart_id=cart_id, product_id=product_id, quantity=quantity)
        except Exception as e:
            raise e
