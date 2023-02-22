from app.db.database import SessionLocal

from app.products.repositories import ProductTypeRepository


class ProductTypeServices:

    @staticmethod
    def create_product_type(product_type: str):
        """
            Creates a new product type with the given name.

            :param product_type: The name of the product type to create.
            :return: The created product type.
            :raises Exception: If an error occurs while creating the product type.
            """

        with SessionLocal() as db:
            try:
                product_repository = ProductTypeRepository(db)
                return product_repository.create_product_type(product_type=product_type)
            except Exception as e:
                raise e

    @staticmethod
    def get_product_type_by_id(product_type_id: str):
        """
            Retrieves a product type by its ID.

            :param product_type_id: The ID of the product type to retrieve.
            :return: The retrieved product type.
            :raises Exception: If an error occurs while retrieving the product type.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.get_product_type_by_id(product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_product_types():
        """
            Retrieves all product types.

            :return: A list of all product types.
            :raises Exception: If an error occurs while retrieving the product types.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.get_all_product_types()
        except Exception as e:
            raise e

    @staticmethod
    def update_product_type(product_type_id: str, product_type: str):
        """
            Updates the name of an existing product type.

            :param product_type_id: The ID of the product type to update.
            :param product_type: The new name of the product type.
            :return: The updated product type.
            :raises Exception: If an error occurs while updating the product type.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.update_product_type(product_type_id=product_type_id,
                                                              product_type=product_type)
        except Exception as e:
            raise e

    @staticmethod
    def delete_product_type_by_id(product_type_id):
        """
            Deletes a product type by its ID.

            :param product_type_id: The ID of the product type to delete.
            :return: True if the product type was deleted successfully, False otherwise.
            :raises Exception: If an error occurs while deleting the product type.
            """
        try:
            with SessionLocal() as db:
                product_repository = ProductTypeRepository(db)
                return product_repository.delete_product_type_by_id(product_type_id)
        except Exception as e:
            raise e
