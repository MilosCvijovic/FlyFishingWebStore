from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions import ProductTypeNotFoundException
from app.products.models import ProductType


class ProductTypeRepository:
    """This class contains methods to interact with the 'product_types' table in the database."""
    def __init__(self, db: Session):
        """Initialize the ProductTypeRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_product_type(self, product_type: str):
        """Create a new product type in the database.

           :param product_type: The name of the new product type.
           :raises IntegrityError: If the product type already exists in the database.
           :return: The newly created ProductType object.
           """
        try:
            product = ProductType(product_type=product_type)
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            raise e

    def get_product_type_by_id(self, product_type_id: str):
        """Get a product type by its ID from the database.

           :param product_type_id: The ID of the product type to retrieve.
           :raises ProductTypeNotFoundException: If a product type with the provided ID does not exist in the database.
           :return: The ProductType object corresponding to the provided ID.
           """
        product = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
        if product is None:
            raise ProductTypeNotFoundException(f"Product with provided ID {product_type_id} not found", 400)
        return product

    def get_all_product_types(self):
        """Get all product types from the database.

           :return: A list of ProductType objects.
           """
        products = self.db.query(ProductType).all()
        return products

    def update_product_type(self, product_type_id: str, product_type: str):
        """Update an existing product type in the database.

            :param product_type_id: The ID of the product type to update.
            :param product_type: The new name of the product type.
            :raises ProductTypeNotFoundException: If a product type with the provided ID does not exist in the database.
            :return: The updated ProductType object.
            """
        try:
            product = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            if product is None:
                raise ProductTypeNotFoundException(f"Product with provided ID {product_type_id} not found", 400)

            if product_type is not None:
                product.product_type = product_type

            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e

    def delete_product_type_by_id(self, product_type_id: str):
        """Delete a product type by its ID from the database.

            :param product_type_id: The ID of the product type to delete.
            :raises ProductTypeNotFoundException: If a product type with the provided ID does not exist in the database.
            :return: True if the product type was successfully deleted.
            """
        try:
            product = self.db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
            if product is None:
                raise ProductTypeNotFoundException(f"Product with provided ID {product_type_id} not found", 400)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e
