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
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        return product

    def create_new_rod(self, brand: str, model: str, length: int, weight: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
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
        rod = self.db.query(Rod).filter(Rod.rod_id == rod_id).first()
        if rod is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {rod_id} not found", 400)
        return rod

    def get_rods_by_brand_name(self, brand: str):
        """Get rod by their first name.

        :param brand: The first name of the rod to retrieve.
        :return: A list of Employee instances
        :raises: EmployeeNotFoundException: If no rod are found with the given first name"""
        rod = self.db.query(Rod).filter(Rod.brand.like(brand + "%")).all()
        if rod is None:
            raise RodNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return rod

    def get_all_rods(self):
        """Get all rods in the database.

        :return: A list of all Employee instances"""
        rods = self.db.query(Rod).all()
        return rods

    def delete_rod_by_id(self, rod_id: str):
        """Deletes a rod by ID.

        :return: True if the rod was deleted successfully, False otherwise."""
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

    def update_rod(self, rod_id: str, brand: str = None, model: str = None, length: int = None,
                        weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                        description: str = None, in_stock: bool = None, product_id: str = None,
                        product_type_id: str = None):

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



