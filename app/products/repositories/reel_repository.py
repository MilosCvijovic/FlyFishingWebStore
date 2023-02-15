from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException, ReelNotFoundException
from app.products.models import Reel, ProductType


class ReelRepository:
    """This class contains methods to interact with the 'rods' table in the database."""

    def __init__(self, db: Session):
        """Initialize the RodRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_new_reel(self, brand: str, model: str, weight: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_type_id: str):
        try:
            product_type = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            reel = Reel(brand=brand, model=model, weight=weight, AFTM=AFTM, price=price,
                        quantity=quantity, description=description, in_stock=in_stock,
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
            self.db.delete(reel)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_reel(self, reel_id: str, brand: str = None, model: str = None,
                    weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                    description: str = None, in_stock: bool = None, product_type_id: str = None):
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
            self.db.commit()
            self.db.refresh(reel)
            return reel
        except Exception as e:
            raise e



