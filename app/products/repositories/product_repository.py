from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductNotFoundException
from app.products.models import Product, ProductType


class ProductRepository:
    """This class contains methods to interact with the 'rods' table in the database."""

    def __init__(self, db: Session):
        """Initialize the RodRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_new_product(self, brand: str, model: str, price: int):
        try:
            product = Product(brand=brand, model=model, price=price)
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            raise e

    def get_product_by_id(self, product_id: str):
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        if product is None:
            raise ProductNotFoundException(f"Product with provided ID {product_id} not found", 400)
        return product

    def get_products_by_brand_name(self, brand: str):
        """Get products by their first name.

        :param brand: The first name of the products to retrieve.
        :return: A list of Employee instances
        :raises: EmployeeNotFoundException: If no products are found with the given first name"""
        products = self.db.query(Product).filter(Product.brand.like(brand + "%")).all()
        if products is None:
            raise ProductNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return products

    def get_all_products(self):
        """Get all products in the database.

        :return: A list of all Employee instances"""
        products = self.db.query(Product).all()
        return products

    def delete_product_by_id(self, product_id: str):
        """Deletes a product by ID.

        :return: True if the product was deleted successfully, False otherwise."""
        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                raise ProductNotFoundException(f"Rod with provided ID: {product_id} not found.", 400)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_product(self, product_id: str, brand: str = None, model: str = None, price: int = None):

        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                raise ProductNotFoundException(f"Rod with provided ID: {product_id} not found.", 400)
            if brand is not None:
                product.brand = brand
            if model is not None:
                product.model = model
            if price is not None:
                product.price = price
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e
