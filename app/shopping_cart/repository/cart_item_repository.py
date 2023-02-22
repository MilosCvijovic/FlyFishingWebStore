from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.models import Product
from app.shopping_cart.exceptions import CartItemNotFoundException
from app.shopping_cart.models import CartItem


class CartItemRepository:
    """This class contains methods to interact with the 'cart items' table in the database."""

    def __init__(self, db: Session):
        """Initialize the CartItemRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_new_cart_item(self, quantity: int, product_id: str, shopping_cart_id: str):
        """Create a new cart item and add it to the database.

            :param quantity: The quantity of the product in the cart.
            :param product_id: The ID of the product being added to the cart.
            :param shopping_cart_id: The ID of the shopping cart to which the cart item belongs.
            :return: A new CartItem instance representing the added cart item.
            :raises IntegrityError: If the provided product ID is not found in the database."""
        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            total_price = quantity * product.price
            cart_item = CartItem(quantity=quantity, price=product.price, total_price=total_price,
                                 product_id=product_id, shopping_cart_id=shopping_cart_id)
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        except IntegrityError as e:
            raise e

    def get_cart_item_by_id(self, cart_id: str):
        """Get a cart item by ID.

            :param cart_id: The ID of the cart item to retrieve.
            :return: A CartItem instance representing the retrieved cart item.
            :raises CartItemNotFoundException: If a cart item with the provided ID is not found in the database."""
        cart_item = self.db.query(CartItem).filter(CartItem.cart_id == cart_id).first()
        if cart_item is None:
            raise CartItemNotFoundException(f"CatItem with provided ID {cart_id} not found", 400)
        return cart_item

    def get_all_cart_items(self):
        """Get all cart items in the database.

        :return: A list of all Cart items"""
        cart_items = self.db.query(CartItem).all()
        return cart_items

    def delete_cart_item_by_id(self, cart_id: str):
        """Deletes a cart_item by ID.

        :return: True if the cart_item was deleted successfully, False otherwise."""
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_id == cart_id).first()
            if cart_item is None:
                raise CartItemNotFoundException(f"Rod with provided ID: {cart_id} not found.", 400)
            self.db.delete(cart_item)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_cart_item(self, cart_id: str, product_id: str, quantity: int = None):
        """Update a cart item.

           :param cart_id: The ID of the cart item to update.
           :param product_id: The ID of the product to associate with the cart item. If not provided,
           the product ID will not be updated.
           :param quantity: The new quantity of the product in the cart. If not provided, the quantity
           will not be updated.
           :return: A CartItem instance representing the updated cart item."""
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_id == cart_id).first()
            if cart_item is None:
                raise CartItemNotFoundException(f"Cart item with provided ID: {cart_id} not found.", 400)
            if product_id is not None:
                cart_item.product_id = product_id
            if quantity is not None:
                cart_item.quantity = quantity
            cart_item.total_price = cart_item.quantity * cart_item.price
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        except Exception as e:
            raise e
