from app.db.database import SessionLocal
from app.products.repositories import FlyRepository


class FlyServices:
    @staticmethod
    def create_new_fly(brand: str, model: str, length: int, weight: int, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
           Create a new Fly product.

           :param brand: The brand of the Fly product.
           :param model: The model of the Fly product.
           :param length: The length of the Fly product.
           :param weight: The weight of the Fly product.
           :param price: The price of the Fly product.
           :param quantity: The quantity of the Fly product available in stock.
           :param description: The description of the Fly product.
           :param in_stock: A boolean representing whether the Fly product is in stock.
           :param product_id: The ID of the product associated with the Fly product.
           :param product_type_id: The ID of the product type associated with the Fly product.
           :return: The newly created Fly product.
           """
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.create_new_fly(brand=brand, model=model, length=length, weight=weight,
                                                     price=price, quantity=quantity,
                                                     description=description, in_stock=in_stock, product_id=product_id,
                                                     product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_fly_by_id(fly_id: str):
        """
           Get a Fly product by its ID.

           :param fly_id: The ID of the Fly product to retrieve.
           :return: The Fly product with the given ID.
           """
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.get_fly_by_id(fly_id=fly_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_flies_by_brand_name(brand: str):
        """
           Get all Fly products with the given brand name.

           :param brand: The brand name of the Fly products to retrieve.
           :return: A list of all Fly products with the given brand name.
           """
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.get_flies_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_flies():
        """
           Get all Fly products.

           :return: A list of all Fly products.
           """
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.get_all_flies()
        except Exception as e:
            raise e

    @staticmethod
    def delete_fly_by_id(fly_id: str):
        """
            Delete a Fly product by its ID.

            :param fly_id: The ID of the Fly product to delete.
            :return: True if the deletion was successful, False otherwise.
            """
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                fly_repository.delete_fly_by_id(fly_id=fly_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_fly(fly_id: str, brand: str = None, model: str = None, length: int = None,
                   weight: int = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
        """
            Update a Fly product by its ID.

            :param fly_id: The ID of the Fly product to update.
            :param brand: The new brand of the Fly product.
            :param model: The new model of the Fly product.
            :param length: The new length of the Fly product.
            :param weight: The new weight of the Fly product.
            :param price: The new price of the Fly product.
            :param quantity: The new quantity of the Fly product available in stock.
            :param description: The new description of the Fly product.
            :param in_stock: A boolean representing whether the Fly product is in stock.
            :param product_id: The new ID of the product associated with the Fly product.
            :param product_type_id: The new ID of the product type associated with the Fly product.
            :return: The updated Fly product.
            """
        try:
            with SessionLocal() as db:
                fly_repository = FlyRepository(db)
                return fly_repository.update_fly(fly_id=fly_id, brand=brand, model=model, length=length,
                                                 weight=weight, price=price, quantity=quantity,
                                                 description=description, in_stock=in_stock, product_id=product_id,
                                                 product_type_id=product_type_id)
        except Exception as e:
            raise e
