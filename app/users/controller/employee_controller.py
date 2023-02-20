from fastapi import HTTPException, Response

from app.users.exceptions import *
from app.users.services import EmployeeServices, EmployeeTypeServices


class EmployeeController:
    """The EmployeeController class is responsible for managing the creation of employees."""

    @staticmethod
    def create_employee(user_id, employee_type_id):
        """Create a new employee.

        :param first_name: The first name of the employee.
        :param last_name: The last name of the employee.
        :param user_id: The ID of the user associated with the employee.
        :param employee_type_id: The ID of the employee type.

        :return: The newly created employee.

        :raises: HTTPException with status code 500.
                 HTTPException with status code 404 in case the employee type with specified id does not exist."""
        try:
            EmployeeTypeServices.get_employee_type_by_id(employee_type_id)
            employee = EmployeeServices.create_employee(user_id, employee_type_id)
            return employee
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_by_id(employee_id: str):
        """Get the employee by id.

    :param employee_id: The id of the employee.
    :return: The employee instance if found.
    :raises: HTTPException with status code 400."""
        employee = EmployeeServices.get_employee_by_id(employee_id)
        if employee:
            return employee
        raise HTTPException(status_code=400,
                            detail=f"Employee with provided id {employee_id} does not exist")

    @staticmethod
    def get_employees_by_first_name(first_name: str):
        """Get the employees by first name.

    :param first_name: The first name of the employee.
    :return: The employees if it found.
    :raises: HTTPException with status code 400."""
        employees = EmployeeServices.get_employees_by_first_name(first_name)
        if employees:
            return employees
        raise HTTPException(status_code=400,
                            detail=f"Employee with provided characters {first_name} does not exist")

    @staticmethod
    def get_employees_by_employee_type_id(employee_type_id: str):
        """Get the employees by employee type id.

        :param employee_type_id: The id of the employee type.
        :return: The employees if it found.
        :raises: HTTPException with status code 400."""
        employees = EmployeeServices.get_employees_by_employee_type_id(employee_type_id)
        if employees:
            return employees
        raise HTTPException(status_code=400,
                            detail=f"Employee with provided employee type id {employee_type_id} does not exist")

    @staticmethod
    def get_all_employees():
        """Get all the employees.

        :return: List of all employees."""
        employee = EmployeeServices.get_all_employees()
        return employee

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        """Delete the employee by id.

        :param employee_id: The id of the employee.

        :return: True if the employee was deleted successfully, False otherwise.
        :raises: EmployeeNotFoundException.
        :raises: HTTPException with status code 400."""
        try:
            EmployeeServices.delete_employee_by_id(employee_id)
            return Response(content=f"Employee with id - {employee_id} is deleted")
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_employee(employee_id: str, first_name: str = None, last_name: str = None, user_id: str = None,
                        employee_type_id: str = None):
        """Update the employee.

        :param employee_id: The id of the employee.
        :param first_name: The first name of the employee.
        :param last_name: The last name of the employee.
        :param user_id: The id of the user.
        :param employee_type_id: The id of the employee type.

        :return: The updated employee instance.
        :raises: HTTPException with status code 500."""
        try:
            employee = EmployeeServices.update_employee(employee_id, first_name, last_name, user_id, employee_type_id)
            return employee
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
