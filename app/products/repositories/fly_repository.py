from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException, FlyNotFoundException, ProductNotFoundException
from app.products.models import Fly, ProductType, Product


class FlyRepository:
    """This class contains methods to interact with the 'rods' table in the database."""

    def __init__(self, db: Session):
        """Initialize the RodRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def get_product(self, product_id: str):
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        return product

    def create_new_fly(self, brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        try:
            product_type = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            fly = Fly(brand=brand, model=model, length=length, weight=weight, AFTM=AFTM, price=price,
                      quantity=quantity, description=description, in_stock=in_stock, product_id=product_id,
                      product_type_id=product_type.product_type_id)
            self.db.add(fly)
            self.db.commit()
            self.db.refresh(fly)
            return fly
        except IntegrityError as e:
            raise e

    def get_fly_by_id(self, fly_id: str):
        fly = self.db.query(Fly).filter(Fly.fly_id == fly_id).first()
        if fly is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {fly_id} not found", 400)
        return fly

    def get_flies_by_brand_name(self, brand: str):
        """Get fly by their first name.

        :param brand: The first name of the fly to retrieve.
        :return: A list of Employee instances
        :raises: EmployeeNotFoundException: If no fly are found with the given first name"""
        fly = self.db.query(Fly).filter(Fly.brand.like(brand + "%")).all()
        if fly is None:
            raise FlyNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return fly

    def get_all_flies(self):
        """Get all fly in the database.

        :return: A list of all Employee instances"""
        fly = self.db.query(Fly).all()
        return fly

    def delete_fly_by_id(self, fly_id: str):
        """Deletes a fly by ID.

        :return: True if the fly was deleted successfully, False otherwise."""
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

    def update_fly(self, fly_id: str, brand: str = None, model: str = None, length: int = None,
                        weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                        description: str = None, in_stock: bool = None, product_id: str = None,
                        product_type_id: str = None):

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
            if AFTM is not None:
                fly.AFTM = AFTM
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
