from app.users.repository.employee_type_repository import EmployeeTypeRepository
from app.db.database import SessionLocal
from app.users.exceptions import *


class EmployeeTypeServices:
    """
    EmployeeTypeServices is a class containing all the methods that are related to employee types.
    It is a layer between the repository and the views, containing the logic to interact with the database.
    """

    @staticmethod
    def create_employee_type(employee_type: str):
        """
        This method creates a new employee type in the database.

        :param employee_type: The employee type to be created.
        :return: The newly created employee type.
        :raises EmployeeTypeExistsException: If the employee type already exists in the database.
        :raises Exception: If an error occurs while creating the employee type."""
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                new_type = employee_type_repository.read_employee_type_by_type(employee_type)
                if new_type is None:
                    return employee_type_repository.create_employee_type(employee_type)
                raise EmployeeTypeExistsException(message="Type already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_employee_type_by_id(employee_type_id: str):
        """ This method retrieves an employee type from the database by its ID.

        :param employee_type_id: The ID of the employee type to be retrieved.
        :return: The retrieved employee type.
        :raises Exception: If an error occurs while retrieving the employee type."""
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                return employee_type_repository.read_employee_type_by_id(employee_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employee_types():
        """
        This method retrieves all employee types from the database.

        :return: A list of all employee types.
        """
        with SessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            return employee_type_repository.read_all_employee_types()

    @staticmethod
    def delete_employee_type_by_id(employee_type_id: str):
        """This method deletes an employee type from the database by its ID.

        :param employee_type_id: The ID of the employee type to be deleted.
        :return: True if the employee type was deleted successfully, False otherwise.
        :raises Exception: If an error occurs while deleting the employee type."""
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                employee_type_repository.delete_employee_type_by_id(employee_type_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_employee_type(employee_type_id: str, employee_type: str):
        """ Update an existing employee type.

        :param employee_type_id: ID of the employee type to be updated.
        :param employee_type: The new name for the employee type.
        :return: The updated employee type object.
        :raises Exception: If any error occurs while updating the employee type in the database."""
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                return employee_type_repository.update_employee_type(employee_type_id, employee_type)
        except Exception as e:
            raise e
