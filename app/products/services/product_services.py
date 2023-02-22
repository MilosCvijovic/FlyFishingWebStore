from app.db.database import SessionLocal
from app.products.repositories import ProductRepository


class ProductServices:
    @staticmethod
    def create_new_product(brand: str, model: str, price: int):
        """
          Create a new product with the specified brand, model, and price.

          :param brand: The brand of the product.
          :param model: The model of the product.
          :param price: The price of the product.

          :return: A dictionary containing information about the newly created product.
          :raises Exception: If an error occurs while creating the product.
          """
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.create_new_product(brand=brand, model=model, price=price)
        except Exception as e:
            raise e

    @staticmethod
    def get_product_by_id(product_id: str):
        """
            Retrieve a product by its ID.

            :param product_id: The ID of the product.

            :return: A dictionary containing information about the product, or None if the product is not found.
            :raises Exception: If an error occurs while retrieving the product.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.get_product_by_id(product_id=product_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_products_by_brand_name(brand: str):
        """
            Retrieve all products with the specified brand.

            :param brand: The brand of the products to retrieve.

            :return: A list of dictionaries containing information about the products.
            :raises Exception: If an error occurs while retrieving the products.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.get_products_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_products():
        """
            Retrieve all products.

            :return: A list of dictionaries containing information about the products.
            :raises Exception: If an error occurs while retrieving the products.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.get_all_products()
        except Exception as e:
            raise e

    @staticmethod
    def delete_product_by_id(product_id: str):
        """
            Delete a product by its ID.

            :param product_id: The ID of the product to delete.

            :return: True if the product is successfully deleted, otherwise False.
            :raises Exception: If an error occurs while deleting the product.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                product_repository.delete_product_by_id(product_id=product_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_product(product_id: str, brand: str = None, model: str = None, price: int = None):
        """
            Update an existing product with new information.

            :param product_id: The ID of the product to update.
            :param brand: The new brand of the product.
            :param model: The new model of the product.
            :param price: The new price of the product.

            :return: A dictionary containing information about the updated product.
            :raises Exception: If an error occurs while updating the product.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.update_product(product_id=product_id, brand=brand, model=model, price=price)
        except Exception as e:
            raise e
