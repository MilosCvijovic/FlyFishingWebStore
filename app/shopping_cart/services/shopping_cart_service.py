from app.db.database import SessionLocal
from app.shopping_cart.repository import ShoppingCartRepository


class ShoppingCartServices:
    @staticmethod
    def create_shopping_cart(customer_id: str):
        """
        Create a new shopping cart for the given customer.

        :param customer_id: ID of the customer to whom the shopping cart belongs.
        :return: The created shopping cart.
        :raises Exception: If an error occurs while creating the shopping cart.
        """
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.create_new_shopping_cart(customer_id=customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_shopping_cart_by_id(shopping_cart_id: str):
        """
            Retrieve a shopping cart by its ID.

            :param shopping_cart_id: ID of the shopping cart to retrieve.
            :return: The shopping cart with the specified ID.
            :raises Exception: If an error occurs while retrieving the shopping cart.
            """
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.get_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_shopping_carts():
        """
            Retrieve all shopping carts.

            :return: A list of all shopping carts.
            :raises Exception: If an error occurs while retrieving the shopping carts.
            """
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.get_all_shopping_carts()
        except Exception as e:
            raise e

    @staticmethod
    def delete_shopping_cart_by_id(shopping_cart_id: str):
        """
            Delete a shopping cart by its ID.

            :param shopping_cart_id: ID of the shopping cart to delete.
            :return: True if the shopping cart was deleted successfully, False otherwise.
            :raises Exception: If an error occurs while deleting the shopping cart.
            """
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_cart_repository.delete_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_shopping_cart(shopping_cart_id: str, customer_id: str = None):
        """
            Update a shopping cart by its ID.

            :param shopping_cart_id: ID of the shopping cart to update.
            :param customer_id: ID of the customer to whom the shopping cart belongs.
            :return: The updated shopping cart.
            :raises Exception: If an error occurs while updating the shopping cart.
            """
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.update_shopping_cart(shopping_cart_id=shopping_cart_id,
                                                                     customer_id=customer_id)
        except Exception as e:
            raise e
