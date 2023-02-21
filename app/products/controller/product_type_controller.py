from sqlalchemy.exc import IntegrityError

from app.products.exceptions import ProductTypeNotFoundException
from app.products.services.product_type_service import ProductTypeServices
from app.users.services import UserServices, signJWT
from fastapi import HTTPException, Response


class ProductTypeController:
    """Controller class for Product operations."""

    @staticmethod
    def create_product_type(product_type: str):
        """
           Create a new product type.

           :param product_type: str, the name of the product type to be created.
           :return: dict, the newly created product type.
           :raises: HTTPException with status_code 400 if a product type with the same name already exists.
                    HTTPException with status_code 500 for any other error.
           """

        try:
            product = ProductTypeServices.create_product_type(product_type=product_type)
            return product
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Product with provided name: {product_type} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_product_type_by_id(product_id: str):
        """
            Get a product type by its id.

            :param product_id: str, the id of the product type to retrieve.
            :return: dict, the product type object.
            :raises: HTTPException with status_code 400 if a product type with the provided id does not exist.
                     HTTPException with status_code 500 for any other error.
            """
        product = ProductTypeServices.get_product_type_by_id(product_id)
        if product:
            return product
        raise HTTPException(status_code=400, detail=f"Product with provided id {product_id} does not exist")

    @staticmethod
    def get_all_product_types():
        """
           Get all existing product types.

           :return: list, containing all the product types.
           :raises: HTTPException with status_code 500 for any error.
           """
        product = ProductTypeServices.get_all_product_types()
        return product

    @staticmethod
    def update_product_type(product_type_id: str, product_type: str):
        """
            Update an existing product type.

            :param product_type_id: str, the id of the product type to be updated.
            :param product_type: str, the new name of the product type.
            :return: dict, the updated product type.
            :raises: HTTPException with status_code 500 for any error.
            """
        try:
            product = ProductTypeServices.update_product_type(product_type_id=product_type_id,
                                                              product_type=product_type)
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_product_type_by_id(product_type_id: str):
        """
           Delete a product type by its id.

           :param product_type_id: str, the id of the product type to be deleted.
           :return: Response with content indicating the product has been deleted.
           :raises: HTTPException with status_code 400 if a product type with the provided id does not exist.
                    HTTPException with status_code 500 for any other error.
           """
        try:
            ProductTypeServices.delete_product_type_by_id(product_type_id)
            return Response(content=f"Product with provided ID: {product_type_id} is deleted")
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
