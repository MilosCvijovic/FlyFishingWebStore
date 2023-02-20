import uuid

from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload
from app.shopping_cart.exceptions import ShoppingCartNotFoundException
from app.shopping_cart.models import ShoppingCart, CartItem
from app.users.exceptions import CustomerNotFoundException
from app.users.models import Customer


class ShoppingCartRepository:
    """This class contains methods to interact with the 'rods' table in the database."""

    def __init__(self, db: Session):
        """Initialize the RodRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def get_total_price_by_shopping_cart_id(self, shopping_cart_id: str):
        total_price = self.db.query(func.sum(CartItem.total_price)).filter(
            CartItem.shopping_cart_id == shopping_cart_id).scalar()
        return total_price if total_price is not None else 0

    def create_new_shopping_cart(self, customer_id: str):
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer is None:
                raise CustomerNotFoundException(f"Customer with provided ID: {customer_id} not found.", 400)
            shopping_cart = ShoppingCart(customer_id=customer_id)
            self.db.add(shopping_cart)
            self.db.commit()
            self.db.refresh(shopping_cart)
            return shopping_cart
        except IntegrityError as e:
            raise e

    def get_shopping_cart_by_id(self, shopping_cart_id: str):
        shopping_cart = (
            self.db.query(ShoppingCart)
            .options(joinedload(ShoppingCart.cart_items))
            .filter(ShoppingCart.shopping_cart_id == shopping_cart_id)
            .first()
        )
        if shopping_cart is None:
            raise ShoppingCartNotFoundException(f"Shopping cart with ID {shopping_cart_id} not found", 404)
        cart_items = []
        total_price = self.get_total_price_by_shopping_cart_id(shopping_cart_id)
        for item in shopping_cart.cart_items:
            cart_item_dict = item.__dict__
            cart_item_dict['product'] = item.product.__dict__
            cart_item_dict['shopping_cart_id'] = item.shopping_cart_id
            del cart_item_dict['_sa_instance_state']
            cart_items.append(cart_item_dict)

        return {
            'customer_id': shopping_cart.customer_id,
            'shopping_cart_id': shopping_cart.shopping_cart_id,
            'cart_items': cart_items,
            'total_price': total_price
        }

    def get_all_shopping_carts(self):
        shopping_carts = self.db.query(ShoppingCart).all()
        shopping_carts_list = []
        for shopping_cart in shopping_carts:
            cart_items = []
            for item in shopping_cart.cart_items:
                cart_item_dict = item.__dict__
                cart_item_dict['product'] = item.product.__dict__
                cart_item_dict['shopping_cart_id'] = item.shopping_cart_id
                del cart_item_dict['_sa_instance_state']
                cart_items.append(cart_item_dict)

            total_price = self.get_total_price_by_shopping_cart_id(shopping_cart.shopping_cart_id)
            shopping_carts_list.append({
                'customer_id': shopping_cart.customer_id,
                'shopping_cart_id': shopping_cart.shopping_cart_id,
                'cart_items': cart_items,
                'total_price': total_price
            })
        return shopping_carts_list

    def delete_shopping_cart_by_id(self, shopping_cart_id: str):
        """Deletes a shooping_cart by ID.

        :return: True if the shooping_cart was deleted successfully, False otherwise."""
        try:
            shopping_cart = self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
            if shopping_cart is None:
                raise ShoppingCartNotFoundException(f"Rod with provided ID: {shopping_cart_id} not found.", 400)
            self.db.delete(shopping_cart)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_shopping_cart(self, shopping_cart_id: str, customer_id: str = None):
        try:
            shopping_cart = self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
            if shopping_cart is None:
                raise ShoppingCartNotFoundException(f"Shopping cart with provided ID: {shopping_cart_id} not found.", 400)
            if customer_id is not None:
                shopping_cart.customer_id = customer_id

            self.db.add(shopping_cart)
            self.db.commit()
            self.db.refresh(shopping_cart)
            return shopping_cart
        except Exception as e:
            raise e
