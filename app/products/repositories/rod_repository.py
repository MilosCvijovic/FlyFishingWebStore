from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException, RodNotFoundException, ProductNotFoundException
from app.products.models import Rod, ProductType, Product


class RodRepository:
    """This class contains methods to interact with the 'rods' table in the database."""

    def __init__(self, db: Session):
        """Initialize the RodRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def get_product(self, product_id: str):
        """
            Get a product by ID.

            :param product_id: The ID of the product to get.
            :return: The product with the provided ID.
            """
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        return product

    def create_new_rod(self, brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """Create a new rod record in the database.

            :param brand: The brand of the rod.
            :param model: The model of the rod.
            :param length: The length of the rod.
            :param weight: The weight of the rod.
            :param AFTM: The AFTM (Association of Fishing Tackle Manufacturers) rating of the rod.
            :param price: The price of the rod.
            :param quantity: The quantity of the rod.
            :param description: The description of the rod.
            :param in_stock: Whether the rod is in stock.
            :param product_id: The ID of the product to associate with the rod.
            :param product_type_id: The ID of the product type to associate with the rod.
            :return: The newly created Rod instance."""
        try:
            product_type = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            rod = Rod(brand=brand, model=model, length=length, weight=weight, AFTM=AFTM, price=price,
                      quantity=quantity, description=description, in_stock=in_stock, product_id=product_id,
                      product_type_id=product_type.product_type_id)
            self.db.add(rod)
            self.db.commit()
            self.db.refresh(rod)
            return rod
        except IntegrityError as e:
            raise e

    def get_rod_by_id(self, rod_id: str):
        """Retrieve all rods in the database with the provided brand name.

            :param rod_id: The rod_id to search for.
            :return: A list of Rod instances with the provided brand name.
            :raises: RodNotFoundException: If no rods are found with the provided brand name."""

        rod = self.db.query(Rod).filter(Rod.rod_id == rod_id).first()
        if rod is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {rod_id} not found", 400)
        return rod

    def get_rods_by_brand_name(self, brand: str):
        """Retrieve all rods in the database with the provided brand name.

           :param brand: The brand name to search for.
           :return: A list of Rod instances with the provided brand name.
           :raises: RodNotFoundException: If no rods are found with the provided brand name."""

        rod = self.db.query(Rod).filter(Rod.brand.like(brand + "%")).all()
        if rod is None:
            raise RodNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return rod

    def get_all_rods(self):
        """Retrieve all rods from the database.

        :return: A list of all Rod instances in the database."""
        rods = self.db.query(Rod).all()
        return rods

    def delete_rod_by_id(self, rod_id: str):
        """Delete a rod from the database by its ID.

            :param rod_id: The ID of the rod to delete.
            :return: True if the rod was deleted successfully, False otherwise.
            :raises: RodNotFoundException: If no rod is found with the provided ID."""

        try:
            rod = self.db.query(Rod).filter(Rod.rod_id == rod_id).first()
            if rod is None:
                raise RodNotFoundException(f"Rod with provided ID: {rod_id} not found.", 400)
            product_id = rod.product_id
            product = self.get_product(product_id)
            self.db.delete(rod)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_rod(self, rod_id: str, brand: str = None, model: str = None, length: int = None, weight: int = None,
                   AFTM: str = None, price: int = None, quantity: int = None, description: str = None,
                   in_stock: bool = None, product_id: str = None, product_type_id: str = None):
        """Updates an existing rod with the specified ID.

            :param rod_id: The ID of the rod to update.
            :param brand: The new brand of the rod (optional).
            :param model: The new model of the rod (optional).
            :param length: The new length of the rod (optional).
            :param weight: The new weight of the rod (optional).
            :param AFTM: The new AFTM rating of the rod (optional).
            :param price: The new price of the rod (optional).
            :param quantity: The new quantity of the rod in stock (optional).
            :param description: The new description of the rod (optional).
            :param in_stock: Whether the rod is in stock or not (optional).
            :param product_id: The ID of the associated product (optional).
            :param product_type_id: The ID of the associated product type (optional).
            :return: The updated Rod instance.
            :raises RodNotFoundException: If no rod is found with the given ID.
            :raises ProductNotFoundException: If no product is found with the given ID.
            """
        try:
            rod = self.db.query(Rod).filter(Rod.rod_id == rod_id).first()
            if rod is None:
                raise RodNotFoundException(f"Rod with provided ID: {rod_id} not found.", 400)
            if brand is not None:
                rod.brand = brand
            if model is not None:
                rod.model = model
            if length is not None:
                rod.length = length
            if weight is not None:
                rod.weight = weight
            if AFTM is not None:
                rod.AFTM = AFTM
            if price is not None:
                rod.price = price
            if quantity is not None:
                rod.quantity = quantity
            if description is not None:
                rod.description = description
            if in_stock is not None:
                rod.in_stock = in_stock
            if product_type_id is not None:
                rod.product_type_id = product_type_id
            self.db.add(rod)

            if product_id is not None:
                product = self.get_product(product_id)
                if product in None:
                    raise ProductNotFoundException(f"Product with provided ID: {product_id} not found.", 400)
                if brand is not None:
                    product.brand = brand
                if model is not None:
                    product.model = model
                if price is not None:
                    product.price = price
                self.db.add(product)
            self.db.commit()
            self.db.refresh(rod)
            return rod
        except Exception as e:
            raise e
