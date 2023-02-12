from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import CustomerNotFoundException
from app.users.models import Customer


class CustomerRepository:
    """CustomerRepository is a class responsible for managing customer data."""
    def __init__(self, db: Session):
        """Initializes a new instance of the CustomerRepository class.

        :param db: The database session to be used for database operations."""
        self.db = db

    def create_customer(self, first_name, last_name, user_id):
        """Creates a new customer.

        :param first_name: The first name of the customer.
        :param last_name: The last name of the customer.
        :param user_id: The ID of the user associated with the customer.

        :return: The newly created customer.

        :raises: IntegrityError if there is a conflict with the unique constraints in the database."""
        try:
            customer = Customer(first_name=first_name, last_name=last_name, user_id=user_id)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer

        except IntegrityError as e:
            raise e

    def get_all_customers(self):
        """Get all customers in the database.

        :return: A list of all customers."""
        customers = self.db.query(Customer).all()
        return customers

    def delete_customer_by_id(self, customer_id: str):
        """Deletes a customer by ID.

        :return: True if the customer was deleted successfully, False otherwise."""
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer is None:
                raise CustomerNotFoundException(f"Customer with provided ID: {customer_id} not found.", 400)
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def get_customer_by_id(self, customer_id: str):
        """Gets the customer with the specified ID.

        :param customer_id: The ID of the customer.

        :return: The customer with the specified ID.

        :raises: CustomerNotFoundException if a customer with the specified ID is not found."""
        customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
        if customer is None:
            raise CustomerNotFoundException(f"Customer with provided ID: {customer_id} not found.", 400)
        return customer

    def update_customer(self, customer_id: str, first_name: str = None,
                        last_name: str = None, user_id: str = None):
        """Update a customer by their ID.

        :param customer_id: The ID of the customer to update
        :param first_name: (Optional) The updated first name of the customer
        :param last_name: (Optional) The updated last name of the customer
        :param user_id: (Optional) The updated user ID of the customer

        :return: The updated Customer instance
        :raises: CustomerNotFoundException: If no customer is found with the given ID"""
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer is None:
                raise CustomerNotFoundException(f"Customer with provided ID: {customer_id} not found.", 400)
            if first_name is not None:
                customer.name = first_name
            if last_name is not None:
                customer.last_name = last_name
            if user_id is not None:
                customer.user_id = user_id
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception as e:
            raise e
