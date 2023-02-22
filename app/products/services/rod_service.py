from app.db.database import SessionLocal
from app.products.repositories import RodRepository


class RodServices:
    @staticmethod
    def create_new_rod(brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Create a new rod with the provided details.

            :param brand: The brand of the rod.
            :param model: The model of the rod.
            :param length: The length of the rod.
            :param weight: The weight of the rod.
            :param AFTM: The AFTM rating of the rod.
            :param price: The price of the rod.
            :param quantity: The quantity of the rod available.
            :param description: The description of the rod.
            :param in_stock: Whether the rod is in stock or not.
            :param product_id: The product ID of the rod.
            :param product_type_id: The product type ID of the rod.

            :return: The created rod object.

            :raises: Any exceptions raised by the database or repository.
            """
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.create_new_rod(brand=brand, model=model, length=length, weight=weight,
                                                     AFTM=AFTM, price=price, quantity=quantity,
                                                     description=description, in_stock=in_stock, product_id=product_id,
                                                     product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_rod_by_id(rod_id: str):
        """
           Retrieve a rod by its ID.

           :param rod_id: The ID of the rod.
           :return: The rod object with the provided ID.
           :raises: Any exceptions raised by the database or repository.
           """
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.get_rod_by_id(rod_id=rod_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_rods_by_brand_name(brand: str):
        """
            Retrieve all rods with a given brand name.

            :param brand: The name of the brand.
            :return: A list of rod objects with the provided brand name.
            :raises: Any exceptions raised by the database or repository.
            """
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.get_rods_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_rods():
        """
           Retrieve all rods.

           :return: A list of all rod objects.
           :raises: Any exceptions raised by the database or repository.
           """
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.get_all_rods()
        except Exception as e:
            raise e

    @staticmethod
    def delete_rod_by_id(rod_id: str):
        """
            Delete a rod by its ID.

            :param rod_id: The ID of the rod.
            :return: True if the rod was deleted successfully.
            :raises: Any exceptions raised by the database or repository.
            """
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                rod_repository.delete_rod_by_id(rod_id=rod_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_rod(rod_id: str, brand: str = None, model: str = None, length: int = None,
                   weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
        """
            Update a rod by its ID.

            :param rod_id: The ID of the rod to update.
            :param brand: The new brand name of the rod.
            :param model: The new model name of the rod.
            :param length: The new length of the rod in feet.
            :param weight: The new weight of the rod in ounces.
            :param AFTM: The new AFTM rating of the rod.
            :param price: The new price of the rod in cents.
            :param quantity: The new quantity of the rod in stock.
            :param description: The new description of the rod.
            :param in_stock: The new availability status of the rod.
            :param product_id: The new ID of the product associated with the rod.
            :param product_type_id: The new ID of the product type associated with the rod.
            :return: A dictionary containing the updated rod's information.
            :raises ValueError: If no fields are provided to update or the provided rod ID does not exist.
            :raises Exception: If there is an error while updating the rod.
            """
        try:
            with SessionLocal() as db:
                rod_repository = RodRepository(db)
                return rod_repository.update_rod(rod_id=rod_id, brand=brand, model=model, length=length,
                                                 weight=weight, AFTM=AFTM, price=price, quantity=quantity,
                                                 description=description, in_stock=in_stock, product_id=product_id,
                                                 product_type_id=product_type_id)
        except Exception as e:
            raise e
