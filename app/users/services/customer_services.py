from app.db.database import SessionLocal
from app.users.repository.customer_repository import CustomerRepository


class CustomerServices:
    @staticmethod
    def create_customer(first_name, last_name, user_id):
        """Creates an employee in the database.

        :param first_name: The first name of the customer.
        :param last_name: The last name of the customer.
        :param user_id: The ID of the user.
        :return: The ID of the newly created customer.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.create_customer(first_name, last_name, user_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_customer_by_id(customer_id: str):
        """Retrieves an employee by ID.

        :param customer_id: The ID of the ecustomer.
        :return: The customer with the specified ID.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_customer_by_id(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_customers():
        """Retrieve all customers.

        :return: List of all customers in the database.
        :raises: Exception."""
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_all_customers()
        except Exception as e:
            raise e

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        """Deletes a customer by ID.

        :param customer_id: The ID of the employee.
        :return: True if the customer was deleted successfully, False otherwise.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customer_repository.delete_customer_by_id(customer_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_customer(customer_id: str, first_name: str = None, last_name: str = None, user_id: str = None):
        """Updates an employee with the specified ID.

        :param customer_id: The ID of the customer.
        :param first_name: The first name of the customer.
        :param last_name: The last name of the customer.
        :param user_id: The ID of the user.
        :return: The updated employee.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.update_customer(customer_id, first_name, last_name, user_id)
        except Exception as e:
            raise e
