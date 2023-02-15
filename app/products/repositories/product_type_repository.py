from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException
from app.products.models import ProductType


class ProductTypeRepository:
    """This class contains methods to interact with the 'products' table in the database."""
    def __init__(self, db: Session):
        """Initialize the ProductRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_product_type(self, product_type: str):
        try:
            product = ProductType(product_type=product_type)
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            raise e

    def get_product_type_by_id(self, product_type_id: str):
        product = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
        if product is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {product_type_id} not found", 400)
        return product

    def get_all_product_types(self):
        products = self.db.query(ProductType).all()
        return products

    def update_product_type(self, product_type_id: str, product_type: str):
        try:
            product = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            if product is None:
                raise ProductTypeNotFoundException(f"Product with provided ID {product_type_id} not found", 400)

            if product_type is not None:
                product.product_type = product_type

            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
        except Exception as e:
            raise e

    def delete_product_type_by_id(self, product_type_id: str):
        try:
            product = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            if product is None:
                raise ProductTypeNotFoundException(f"Product with provided ID {product_type_id} not found", 400)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e
