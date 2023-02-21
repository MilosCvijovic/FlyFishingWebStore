from fastapi import HTTPException, Response
from app.products.services import ProductServices
from app.products.exceptions import *


class ProductController:
    """Controller class for handling HTTP requests related to products."""

    @staticmethod
    def create_new_product(brand: str, model: str, price: int):
        """
            Create a new product with the specified brand, model, and price.

            :param brand: The brand of the new product.
            :param model: The model of the new product.
            :param price: The price of the new product.
            :return: A dictionary containing the details of the newly created product.
            :raises HTTPException: If an error occurs while creating the product.
            """
        try:
            product = ProductServices.create_new_product(brand=brand, model=model, price=price)
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_product_by_id(product_id: str):
        """
            Get the product with the specified ID.

            :param product_id: The ID of the product to retrieve.
            :return: A dictionary containing the details of the specified product.
            :raises HTTPException: If the product with the specified ID is not found.
            """
        product = ProductServices.get_product_by_id(product_id=product_id)
        if product:
            return product
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {product_id} is not exist")

    @staticmethod
    def get_rod_by_brand_name(brand: str):
        """
            Get all products with the specified brand.

            :param brand: The brand of the products to retrieve.
            :return: A list of dictionaries containing the details of the specified products.
            :raises HTTPException: If no products with the specified brand are found.
            """
        products = ProductServices.get_products_by_brand_name(brand=brand)
        if products:
            return products
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_products():
        """
            Get all products.

            :return: A list of dictionaries containing the details of all products.
            """
        products = ProductServices.get_all_products()
        return products

    @staticmethod
    def delete_product_by_id(product_id: str):
        """
            Delete the product with the specified ID.

            :param product_id: The ID of the product to delete.
            :return: A response indicating that the product has been deleted.
            :raises HTTPException: If the product with the specified ID is not found or cannot be deleted.
            """
        try:
            ProductServices.delete_product_by_id(product_id=product_id)
            return Response(content=f"Rod with provided ID: {product_id} is not exist")
        except ProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_product(product_id: str, brand: str = None, model: str = None, price: int = None):
        """
            Update the product with the specified ID.

            :param product_id: The ID of the product to update.
            :param brand: The new brand for the product.
            :param model: The new model for the product.
            :param price: The new price for the product.
            :return: A dictionary containing the details of the updated product.
            :raises HTTPException: If the product with the specified ID is not found or cannot be updated.
            """

        try:
            return ProductServices.update_product(product_id=product_id, brand=brand, model=model, price=price)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
