from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException, LineNotFoundException
from app.products.models import Line, ProductType


class LineRepository:
    """This class contains methods to interact with the 'rods' table in the database."""

    def __init__(self, db: Session):
        """Initialize the RodRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_new_line(self, brand: str, model: str, length: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_type_id: str):
        try:
            product_type = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            line = Line(brand=brand, model=model, length=length, AFTM=AFTM, price=price,
                      quantity=quantity, description=description, in_stock=in_stock,
                      product_type_id=product_type.product_type_id)
            self.db.add(line)
            self.db.commit()
            self.db.refresh(line)
            return line
        except IntegrityError as e:
            raise e

    def get_line_by_id(self, line_id: str):
        line = self.db.query(Line).filter(Line.line_id == line_id).first()
        if line is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {line_id} not found", 400)
        return line

    def get_lines_by_brand_name(self, brand: str):
        """Get line by their first name.

        :param brand: The first name of the line to retrieve.
        :return: A list of Employee instances
        :raises: EmployeeNotFoundException: If no line are found with the given first name"""
        line = self.db.query(Line).filter(Line.brand.like(brand + "%")).all()
        if line is None:
            raise LineNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return line

    def get_all_lines(self):
        """Get all lines in the database.

        :return: A list of all Employee instances"""
        lines = self.db.query(Line).all()
        return lines

    def delete_line_by_id(self, line_id: str):
        """Deletes a line by ID.

        :return: True if the line was deleted successfully, False otherwise."""
        try:
            line = self.db.query(Line).filter(Line.line_id == line_id).first()
            if line is None:
                raise LineNotFoundException(f"Rod with provided ID: {line_id} not found.", 400)
            self.db.delete(line)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_line(self, line_id: str, brand: str = None, model: str = None, length: int = None,
                        AFTM: str = None, price: int = None, quantity: int = None,
                        description: str = None, in_stock: bool = None, product_type_id: str = None):

        try:
            line = self.db.query(Line).filter(Line.line_id == line_id).first()
            if line is None:
                raise LineNotFoundException(f"Rod with provided ID: {line_id} not found.", 400)
            if brand is not None:
                line.brand = brand
            if model is not None:
                line.model = model
            if length is not None:
                line.length = length
            if AFTM is not None:
                line.AFTM = AFTM
            if price is not None:
                line.price = price
            if quantity is not None:
                line.quantity = quantity
            if description is not None:
                line.description = description
            if in_stock is not None:
                line.in_stock = in_stock
            if product_type_id is not None:
                line.product_type_id = product_type_id
            self.db.add(line)
            self.db.commit()
            self.db.refresh(line)
            return line
        except Exception as e:
            raise e



