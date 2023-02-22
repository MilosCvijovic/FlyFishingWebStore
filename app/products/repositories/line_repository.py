from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException, LineNotFoundException, ProductNotFoundException
from app.products.models import Line, ProductType, Product


class LineRepository:
    """This class contains methods to interact with the 'lines' table in the database."""

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

    def create_new_line(self, brand: str, model: str, length: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        """Create a new line in the database.

            :param brand: The brand name of the line.
            :param model: The model name of the line.
            :param length: The length of the line in feet.
            :param AFTM: The AFTM (Association of Fishing Tackle Manufacturers) rating of the line.
            :param price: The price of the line.
            :param quantity: The quantity of the line in stock.
            :param description: A description of the line.
            :param in_stock: Whether the line is currently in stock.
            :param product_id: The ID of the product associated with the line.
            :param product_type_id: The ID of the product type associated with the line.
            :return: The newly created Line instance.
            :raises: IntegrityError if there is a database integrity violation."""
        try:
            product_type = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            line = Line(brand=brand, model=model, length=length, AFTM=AFTM, price=price,
                      quantity=quantity, description=description, in_stock=in_stock, product_id=product_id,
                      product_type_id=product_type.product_type_id)
            self.db.add(line)
            self.db.commit()
            self.db.refresh(line)
            return line
        except IntegrityError as e:
            raise e

    def get_line_by_id(self, line_id: str):
        """Retrieve a line from the database by its ID.

            :param line_id: The ID of the line to retrieve.
            :return: The Line instance with the specified ID.
            :raises: LineNotFoundException if no line is found with the given ID."""
        line = self.db.query(Line).filter(Line.line_id == line_id).first()
        if line is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {line_id} not found", 400)
        return line

    def get_lines_by_brand_name(self, brand: str):
        """Retrieve all lines in the database that match the given brand name.

        :param brand: The brand name to search for.
        :return: A list of Line instances matching the given brand name.
        :raises: LineNotFoundException if no lines are found with the given brand name."""
        line = self.db.query(Line).filter(Line.brand.like(brand + "%")).all()
        if line is None:
            raise LineNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return line

    def get_all_lines(self):
        """Retrieve all lines in the database.

        :return: A list of all Line instances."""
        lines = self.db.query(Line).all()
        return lines

    def delete_line_by_id(self, line_id: str):
        """Deletes a line by ID.

        :param line_id: The ID of the line to delete.
        :raise LineNotFoundException: If no line is found with the provided ID.
        :return: True if the line was deleted successfully, False otherwise."""
        try:
            line = self.db.query(Line).filter(Line.line_id == line_id).first()
            if line is None:
                raise LineNotFoundException(f"Rod with provided ID: {line_id} not found.", 400)
            product_id = line.product_id
            product = self.get_product(product_id)
            self.db.delete(line)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_line(self, line_id: str, brand: str = None, model: str = None, length: int = None,
                        AFTM: str = None, price: int = None, quantity: int = None,
                        description: str = None, in_stock: bool = None, product_id: str = None,
                        product_type_id: str = None):
        """Update a line with the provided ID.

                        :param line_id: The ID of the line to update.
                        :param brand: The new brand of the line.
                        :param model: The new model of the line.
                        :param length: The new length of the line.
                        :param AFTM: The new AFTM (Association of Fishing Tackle Manufacturers) rating of the line.
                        :param price: The new price of the line.
                        :param quantity: The new quantity of the line.
                        :param description: The new description of the line.
                        :param in_stock: The new stock status of the line.
                        :param product_id: The new product ID associated with the line.
                        :param product_type_id: The new product type ID associated with the line.
                        :return: The updated line object.
                        :raises LineNotFoundException: If no line with the provided ID is found.
                        :raises ProductNotFoundException: If no product with the provided ID is found.
                        """

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
            self.db.refresh(line)
            return line
        except Exception as e:
            raise e
