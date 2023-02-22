from app.db.database import SessionLocal
from app.products.repositories import LineRepository


class LineServices:
    @staticmethod
    def create_new_line(brand: str, model: str, length: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
          Creates a new Line product.

          :param brand: The brand of the Line product.
          :param model: The model of the Line product.
          :param length: The length of the Line product.
          :param AFTM: The AFTM rating of the Line product.
          :param price: The price of the Line product.
          :param quantity: The quantity of the Line product.
          :param description: The description of the Line product.
          :param in_stock: The availability of the Line product.
          :param product_id: The ID of the product associated with the Line product.
          :param product_type_id: The ID of the product type associated with the Line product.

          :return: The new Line product.
          :raises Exception: If an error occurs while creating the Line product.
          """
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.create_new_line(brand=brand, model=model, length=length,
                                                       AFTM=AFTM, price=price, quantity=quantity,
                                                       description=description, in_stock=in_stock,
                                                       product_id=product_id, product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_line_by_id(line_id: str):
        """
            Retrieves a Line product by its ID.

            :param line_id: The ID of the Line product to retrieve.

            :return: The Line product with the specified ID.
            :raises Exception: If an error occurs while retrieving the Line product.
            """
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.get_line_by_id(line_id=line_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_lines_by_brand_name(brand: str):
        """
            Retrieves a list of Line products with the specified brand name.

            :param brand: The brand name to search for.

            :return: A list of Line products with the specified brand name.
            :raises Exception: If an error occurs while retrieving the Line products.
            """
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.get_lines_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_lines():
        """
            Retrieves a list of all Line products.

            :return: A list of all Line products.
            :raises Exception: If an error occurs while retrieving the Line products.
            """
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.get_all_lines()
        except Exception as e:
            raise e

    @staticmethod
    def delete_line_by_id(line_id: str):
        """
            Deletes a Line product by its ID.

            :param line_id: The ID of the Line product to delete.

            :return: True if the Line product was successfully deleted.
            :raises Exception: If an error occurs while deleting the Line product.
            """
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                line_repository.delete_line_by_id(line_id=line_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_line(line_id: str, brand: str = None, model: str = None, length: int = None,
                    AFTM: str = None, price: int = None, quantity: int = None,
                    description: str = None, in_stock: bool = None, product_id: str = None,
                    product_type_id: str = None):
        """Updates an existing Line product with new information.

        :param line_id: The ID of the Line product to update.
        :param brand: The new brand of the Line product.
        :param model: The new model of the Line product.
        :param length: The new length of the Line product.
        :param AFTM: The new AFTM rating of the Line product.
        :param price: The new price of the Line product.
        :param quantity: The new quantity of the Line product.
        :param description: The new description of the Line product.
        :param in_stock: The new availability of the Line product.
        :param product_id: The ID of the product
        :return: The newly created Line product.
        :raises Exception: If an error occurs while creating the Line product."""
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.update_line(line_id=line_id, brand=brand, model=model, length=length,
                                                   AFTM=AFTM, price=price, quantity=quantity,
                                                   description=description, in_stock=in_stock, product_id=product_id,
                                                   product_type_id=product_type_id)
        except Exception as e:
            raise e
