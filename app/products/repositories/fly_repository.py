from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException, FlyNotFoundException, ProductNotFoundException
from app.products.models import Fly, ProductType, Product


class FlyRepository:
    """This class contains methods to interact with the 'flies' table in the database."""

    def __init__(self, db: Session):
        """
        Initialize the FlyRepository with a database session.

        :param db: SQLAlchemy session object.
        :type db: Session
        """
        self.db = db

    def get_product(self, product_id: str):
        """
            Get a product by ID.

            :param product_id: The ID of the product to get.
            :return: The product with the provided ID.
            """
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        return product

    def create_new_fly(self, brand: str, model: str, length: int, weight: int, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """
            Create a new fly.

            :param brand: The brand of the fly.
            :param model: The model of the fly.
            :param length: The length of the fly.
            :param weight: The weight of the fly.
            :param price: The price of the fly.
            :param quantity: The quantity of the fly.
            :param description: The description of the fly.
            :param in_stock: Whether the fly is in stock or not.
            :param product_id: The ID of the product.
            :param product_type_id: The ID of the product type.
            :return: The newly created fly.
            :raises: IntegrityError if there is a conflict with unique database constraints.
            """
        try:
            product_type = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            fly = Fly(brand=brand, model=model, length=length, weight=weight, price=price,
                      quantity=quantity, description=description, in_stock=in_stock, product_id=product_id,
                      product_type_id=product_type.product_type_id)
            self.db.add(fly)
            self.db.commit()
            self.db.refresh(fly)
            return fly
        except IntegrityError as e:
            raise e

    def get_fly_by_id(self, fly_id: str):
        """
           Get a fly by ID.

           :param fly_id: The ID of the fly to get.
           :return: The fly with the provided ID.
           :raise ProductTypeNotFoundException: If no fly is found with the provided ID.
           """
        fly = self.db.query(Fly).filter(Fly.fly_id == fly_id).first()
        if fly is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {fly_id} not found", 400)
        return fly

    def get_flies_by_brand_name(self, brand: str):
        """
           Get all flies with a certain brand name.

           :param brand: The brand name to filter by.
           :return: A list of all flies with the provided brand name.
           :raise FlyNotFoundException: If no flies are found with the provided brand name.
           """
        fly = self.db.query(Fly).filter(Fly.brand.like(brand + "%")).all()
        if fly is None:
            raise FlyNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return fly

    def get_all_flies(self):
        """Get all fly in the database.

        :return: A list of all Flies"""
        fly = self.db.query(Fly).all()
        return fly

    def delete_fly_by_id(self, fly_id: str):
        """
        Delete a fly by ID.

        :param fly_id: The ID of the fly to delete.
        :return: True if the fly was deleted successfully, False otherwise.
        :raise FlyNotFoundException: If no fly is found with the provided ID."""
        try:
            fly = self.db.query(Fly).filter(Fly.fly_id == fly_id).first()
            if fly is None:
                raise FlyNotFoundException(f"Rod with provided ID: {fly_id} not found.", 400)
            product_id = fly.product_id
            product = self.get_product(product_id)
            self.db.delete(fly)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_fly(self, fly_id: str, brand: str = None, model: str = None, length: int = None, weight: int = None,
                   price: int = None, quantity: int = None, description: str = None, in_stock: bool = None,
                   product_id: str = None, product_type_id: str = None):
        """Update a fly with the provided ID.

            :param fly_id: The ID of the fly to update.
            :param brand: The new brand of the fly.
            :param model: The new model of the fly.
            :param length: The new length of the fly.
            :param weight: The new weight of the fly.
            :param price: The new price of the fly.
            :param quantity: The new quantity of the fly.
            :param description: The new description of the fly.
            :param in_stock: The new stock status of the fly.
            :param product_id: The new product ID associated with the fly.
            :param product_type_id: The new product type ID associated with the fly.
            :return: The updated fly object.
            :raises FlyNotFoundException: If no fly with the provided ID is found.
            :raises ProductNotFoundException: If no product with the provided ID is found.
            """
        try:
            fly = self.db.query(Fly).filter(Fly.fly_id == fly_id).first()
            if fly is None:
                raise FlyNotFoundException(f"Rod with provided ID: {fly_id} not found.", 400)
            if brand is not None:
                fly.brand = brand
            if model is not None:
                fly.model = model
            if length is not None:
                fly.length = length
            if weight is not None:
                fly.weight = weight
            if price is not None:
                fly.price = price
            if quantity is not None:
                fly.quantity = quantity
            if description is not None:
                fly.description = description
            if in_stock is not None:
                fly.in_stock = in_stock
            if product_type_id is not None:
                fly.product_type_id = product_type_id
            self.db.add(fly)

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
            self.db.refresh(fly)
            return fly
        except Exception as e:
            raise e
