from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException, ReelNotFoundException, ProductNotFoundException
from app.products.models import Reel, ProductType, Product


class ReelRepository:
    """This class contains methods to interact with the 'rods' table in the database."""

    def __init__(self, db: Session):
        """Initialize the RodRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def get_product(self, product_id: str):
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        return product

    def create_new_reel(self, brand: str, model: str, weight: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        try:
            product_type = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            reel = Reel(brand=brand, model=model, weight=weight, AFTM=AFTM, price=price,
                        quantity=quantity, description=description, in_stock=in_stock, product_id=product_id,
                        product_type_id=product_type.product_type_id)
            self.db.add(reel)
            self.db.commit()
            self.db.refresh(reel)
            return reel
        except IntegrityError as e:
            raise e

    def get_reel_by_id(self, reel_id: str):
        reel = self.db.query(Reel).filter(Reel.reel_id == reel_id).first()
        if reel is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {reel_id} not found", 400)
        return reel

    def get_reels_by_brand_name(self, brand: str):
        """Get reel by their first name.

        :param brand: The first name of the reel to retrieve.
        :return: A list of Employee instances
        :raises: EmployeeNotFoundException: If no reel are found with the given first name"""
        reels = self.db.query(Reel).filter(Reel.brand.like(brand + "%")).all()
        if reels is None:
            raise ReelNotFoundException(f"Reels from this manufacturer: {brand} not found.", 400)
        return reels

    def get_all_reels(self):
        """Get all reels in the database.

        :return: A list of all Employee instances"""
        reels = self.db.query(Reel).all()
        return reels

    def delete_reel_by_id(self, reel_id: str):
        """Deletes a rod by ID.

        :return: True if the reel was deleted successfully, False otherwise."""
        try:
            reel = self.db.query(Reel).filter(Reel.reel_id == reel_id).first()
            if reel is None:
                raise ReelNotFoundException(f"Reel with provided ID: {reel_id} not found.", 400)
            product_id = reel.product_id
            product = self.get_product(product_id)
            self.db.delete(reel)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_reel(self, reel_id: str, brand: str = None, model: str = None,
                    weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                    description: str = None, in_stock: bool = None, product_id: str = None,
                    product_type_id: str = None):
        try:
            reel = self.db.query(Reel).filter(Reel.reel_id == reel_id).first()
            if reel is None:
                raise ReelNotFoundException(f"Reel with provided ID: {reel_id} not found.", 400)
            if brand is not None:
                reel.brand = brand
            if model is not None:
                reel.model = model
            if weight is not None:
                reel.weight = weight
            if AFTM is not None:
                reel.AFTM = AFTM
            if price is not None:
                reel.price = price
            if quantity is not None:
                reel.quantity = quantity
            if description is not None:
                reel.description = description
            if in_stock is not None:
                reel.in_stock = in_stock
            if product_type_id is not None:
                reel.product_type_id = product_type_id
            self.db.add(reel)

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
            self.db.refresh(reel)
            return reel
        except Exception as e:
            raise e



