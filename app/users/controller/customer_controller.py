from fastapi import HTTPException, Response

from app.users.exceptions import *
from app.users.services import CustomerServices


class CustomerController:
    """The CustomerController class is responsible for managing the creation of customers."""

    @staticmethod
    def create_customer(user_id):
        """Create a new customer.

        :param user_id: The ID of the user associated with the customer.
        :return: The newly created employee.
        :raises: HTTPException with status code 500.
                 HTTPException with status code 404 in case the customer type with specified id does not exist."""
        try:
            customer = CustomerServices.create_customer(user_id)
            return customer
        except CustomerExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_id(customer_id: str):
        """Get the employee by id.

    :param customer_id: The id of the customer.
    :return: The customer instance if found.
    :raises: HTTPException with status code 400."""
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            return customer
        raise HTTPException(status_code=400,
                            detail=f"Customer with provided id {customer_id} does not exist")

    @staticmethod
    def get_all_customers():
        """Get all customers.

        :return: List of all customers."""
        customer = CustomerServices.get_all_customers()
        return customer

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        """Delete the customer by id.

        :param customer_id: The id of the employee.

        :return: True if the customer was deleted successfully, False otherwise.
        :raises: EmployeeNotFoundException.
        :raises: HTTPException with status code 400."""
        try:
            CustomerServices.delete_customer_by_id(customer_id)
            return Response(content=f"Customer with ID: {customer_id} is deleted")
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_customer(customer_id: str, first_name: str = None, last_name: str = None, user_id: str = None):
        """Update the customer.

        :param customer_id: The id of the customer.
        :param first_name: The first name of the customer.
        :param last_name: The last name of the customer.
        :param user_id: The id of the user.
        :return: The updated customer instance.
        :raises: HTTPException with status code 500."""
        try:
            customer = CustomerServices.update_customer(customer_id, first_name, last_name, user_id)
            return customer
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
