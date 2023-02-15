from app.db.database import SessionLocal
from app.users.repository.employee_repository import EmployeeRepository


class EmployeeServices:
    @staticmethod
    def create_employee(user_id, employee_type_id):
        """Creates an employee in the database.

        :param employee_type_id: The ID of the employee type.
        :param user_id: The ID of the user.
        :return: The ID of the newly created employee.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.create_employee(user_id, employee_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_employee_by_id(employee_id: str):
        """Retrieves an employee by ID.

        :param employee_id: The ID of the employee.
        :return: The employee with the specified ID.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_employees_by_first_name(first_name: str):
        """Retrieve employees based on their first name.

        :param first_name: The first name of the employees to be retrieved.
        :return: List of employees with the specified first name.
        :raises: Exception."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employees_by_first_name(first_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_employees_by_employee_type_id(employee_type_id: str):
        """Retrieve employees based on their employee type ID.

        :param employee_type_id: The ID of the employee type of the employees to be retrieved.
        :return: List of employees with the specified employee type ID.
        :raises: Exception."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employees_by_employee_type_id(employee_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employees():
        """Retrieve all employees.

        :return: List of all employees in the database.
        :raises: Exception."""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        """Deletes an employee by ID.

        :param employee_id: The ID of the employee.
        :return: True if the employee was deleted successfully, False otherwise.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee_repository.delete_employee_by_id(employee_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_employee(employee_id: str, first_name: str = None, last_name: str = None, user_id: str = None,
                        employee_type_id: str = None):
        """Updates an employee with the specified ID.

        :param employee_id: The ID of the employee.
        :param first_name: The first name of the employee.
        :param last_name: The last name of the employee.
        :param user_id: The ID of the user.
        :param employee_type_id: The ID of the employee type.
        :return: The updated employee.
        :raises: Exception"""
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.update_employee(employee_id=employee_id, first_name=first_name,
                                                           last_name=last_name, user_id=user_id,
                                                           employee_type_id=employee_type_id)
        except Exception as e:
            raise e
