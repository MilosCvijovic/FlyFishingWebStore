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

    def create_new_product(self, brand: str, model: str, price: int):
        """Create a new product in the database with the given brand, model, and price.

           :param brand: The brand of the product to create.
           :param model: The model of the product to create.
           :param price: The price of the product to create.
           :return: The newly created Product instance.
           :raises: IntegrityError: If the product already exists in the database with the same ID."""
        try:
            product = Product(brand=brand, model=model, price=price)
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            raise e

    def get_product_by_id(self, product_id: str):
        """Retrieve a product from the database by its ID.

            :param product_id: The ID of the product to retrieve.
            :return: The Product instance corresponding to the provided ID.
            :raises: ProductNotFoundException: If no product is found with the provided ID."""
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        if product is None:
            raise ProductNotFoundException(f"Product with provided ID {product_id} not found", 400)
        return product

    def get_products_by_brand_name(self, brand: str):
        """Retrieve all products from the database with the provided brand name.

        :param brand: The brand name of the products to retrieve.
        :return: A list of Product instances corresponding to the provided brand name.
        :raises: ProductNotFoundException: If no products are found with the provided brand name."""

        products = self.db.query(Product).filter(Product.brand.like(brand + "%")).all()
        if products is None:
            raise ProductNotFoundException(f"Rods from this manufacturer: {brand} not found.", 400)
        return products

    def get_all_products(self):
        """Retrieve all products from the database.

        :return: A list of all Product instances in the database."""
        products = self.db.query(Product).all()
        return products

    def delete_product_by_id(self, product_id: str):
        """Delete a product from the database by its ID.

        :param product_id: The ID of the product to delete.
        :return: True if the product was deleted successfully, False otherwise.
        :raises: ProductNotFoundException: If no product is found with the provided ID."""

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
        """Update a product in the database with the provided fields.

            :param product_id: The ID of the product to update.
            :param brand: The new brand of the product.
            :param model: The new model of the product.
            :param price: The new price of the product.
            :return: The updated Product instance.
            :raises: ProductNotFoundException: If no product is found with the provided ID."""
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
