from app.db.database import SessionLocal
from app.products.repositories import ReelRepository


class ReelServices:
    @staticmethod
    def create_new_reel(brand: str, model: str, weight: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Creates a new reel in the database.

            :param brand: str, the brand of the reel.
            :param model: str, the model of the reel.
            :param weight: int, the weight of the reel.
            :param AFTM: str, the AFTM rating of the reel.
            :param price: int, the price of the reel.
            :param quantity: int, the quantity of the reel.
            :param description: str, the description of the reel.
            :param in_stock: bool, indicates whether the reel is in stock or not.
            :param product_id: str, the ID of the product the reel belongs to.
            :param product_type_id: str, the ID of the product type the reel belongs to.

            :return: dict, the created data.
            :raises Exception: if an error occurs while creating the reel.
            """
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.create_new_reel(brand=brand, model=model, weight=weight,
                                                       AFTM=AFTM, price=price, quantity=quantity,
                                                       description=description, in_stock=in_stock,
                                                       product_id=product_id, product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_reel_by_id(reel_id: str):
        """
            Retrieves a reel by its ID.

            :param reel_id: str, the ID of the reel.

            :return: dict, the retrieved reel data.
            :raises Exception: if an error occurs while retrieving the reel.
            """
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.get_reel_by_id(reel_id=reel_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_reels_by_brand_name(brand: str):
        """
            Retrieves reels by their brand name.

            :param brand: str, the name of the brand.

            :return: list, a list of retrieved reel data.
            :raises Exception: if an error occurs while retrieving reels by brand name.
            """
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.get_reels_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_reels():
        """
            Retrieves all reels.

            :return: list, a list of retrieved reel data.
            :raises Exception: if an error occurs while retrieving all reels.
            """
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.get_all_reels()
        except Exception as e:
            raise e

    @staticmethod
    def delete_reel_by_id(reel_id: str):
        """
            Deletes a reel by its ID.

            :param reel_id: str, the ID of the reel.

            :return: bool, True if the reel was deleted successfully.
            :raises Exception: if an error occurs while deleting the reel.
            """
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                reel_repository.delete_reel_by_id(reel_id=reel_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_reel(reel_id: str, brand: str = None, model: str = None, weight: int = None, AFTM: str = None,
                    price: int = None, quantity: int = None, description: str = None, in_stock: bool = None,
                    product_id: str = None, product_type_id: str = None):
        """
           Updates an existing reel in the database.

           :param reel_id: str, the ID of the reel to update.
           :param brand: str, optional parameter to update the brand of the reel.
           :param model: str, optional parameter to update the model of the reel.
           :param weight: int, optional parameter to update the weight of the reel.
           :param AFTM: str, optional parameter to update the AFTM rating of the reel.
           :param price: int, optional parameter to update the price of the reel.
           :param quantity: int, optional parameter to update the quantity of the reel.
           :param description: str, optional parameter to update the description of the reel.
           :param in_stock: bool, optional parameter to update whether the reel is in stock or not.
           :param product_id: str, optional parameter to update the ID of the product the reel belongs to.
           :param product_type_id: str, optional parameter to update the ID of the product type the reel belongs to.

           :return: dict, the updated data.
           :raises Exception: if an error occurs while updating the reel.
           """
        try:
            with SessionLocal() as db:
                reel_repository = ReelRepository(db)
                return reel_repository.update_reel(reel_id=reel_id, brand=brand, model=model, weight=weight, AFTM=AFTM,
                                                   price=price, quantity=quantity, description=description,
                                                   product_id=product_id, in_stock=in_stock,
                                                   product_type_id=product_type_id)
        except Exception as e:
            raise e
