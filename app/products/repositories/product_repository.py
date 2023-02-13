from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductNotFoundException
from app.products.models import Product


class ProductRepository:
    """This class contains methods to interact with the 'products' table in the database."""
    def __init__(self, db: Session):
        """Initialize the ProductRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_product(self, name: str, price: float, quantity: int, description: str):
        try:
            product = Product(name=name, price=price, quantity=quantity, description=description)
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

    def get_all_products(self):
        products = self.db.query(Product).all()
        return products

    def update_product(self, product_id: str, name: str, price: float, quantity: int, description: str):
        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                raise ProductNotFoundException(f"Product with provided ID {product_id} not found", 400)
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity
            if description is not None:
                product.description = description
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
        except Exception as e:
            raise e

    def delete_product_by_id(self, product_id: str):
        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                raise ProductNotFoundException(f"Product with provided ID {product_id} not found", 400)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e
