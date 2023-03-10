from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.shopping_cart.exceptions import OrderNotFoundException, ShoppingCartNotFoundException
from app.shopping_cart.models import Order, ShoppingCart


class OrderRepository:
    """This class contains methods to interact with the 'orders' table in the database."""

    def __init__(self, db: Session):
        """Initialize the OrderRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_new_order(self, shopping_cart_id: str):
        """Create a new order.

            :param shopping_cart_id: ID of the shopping cart associated with the order.
            :return: The newly created order."""
        try:
            order = Order(shopping_cart_id=shopping_cart_id)
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except IntegrityError as e:
            raise e

    def get_order_by_id(self, order_id: str):
        """Get an order by ID.

            :param order_id: ID of the order to retrieve.
            :return: The order with the specified ID."""
        order = self.db.query(Order).filter(Order.order_id == order_id).first()
        if order is None:
            raise OrderNotFoundException(f"Product with provided ID {order_id} not found", 400)
        return order

    def get_all_orders(self):
        """Get all orders in the database.

        :return: A list of all orders"""
        order = self.db.query(Order).all()
        return order

    def delete_order_by_id(self, order_id: str):
        """Deletes an order by ID.

        :return: True if the order was deleted successfully, False otherwise."""
        try:
            order = self.db.query(Order).filter(Order.order_id == order_id).first()
            if order is None:
                raise OrderNotFoundException(f"Rod with provided ID: {order_id} not found.", 400)
            self.db.delete(order)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def mark_order_as_sent(self, order_id: str, shopping_cart_id: str, sent: bool = False):
        """Mark an order as sent and clear the associated shopping cart.

            :param order_id: ID of the order to mark as sent.
            :param shopping_cart_id: ID of the shopping cart associated with the order.
            :param sent: Boolean indicating whether the order has been sent.
            :return: The updated order."""
        order = self.db.query(Order).filter(Order.order_id == order_id).first()
        if order is None:
            raise OrderNotFoundException(f"Order with ID {order_id} not found", 404)

        shopping_cart = self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
        if shopping_cart is None:
            raise ShoppingCartNotFoundException(f"Shopping cart with ID {shopping_cart_id} not found", 404)

        if sent == True:
            order.sent = True
            self.db.commit()

            if shopping_cart.cart_items:
                for cart_item in shopping_cart.cart_items:
                    self.db.delete(cart_item)

                shopping_cart.cart_items = []

            self.db.commit()
            self.db.refresh(order)

        return order
