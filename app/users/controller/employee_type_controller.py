from app.users.services import EmployeeTypeServices
from fastapi import HTTPException, Response
from app.users.exceptions import *


class EmployeeTypeController:
    """
    EmployeeTypeController is a class that contains all the methods for handling employee type operations.
    It uses the services provided by the `EmployeeTypeServices` class for performing the actual operations.
    """

    @staticmethod
    def create_employee_type(employee_type: str):
        """
        Create a new employee type with the given name

        :param employee_type: The name of the new employee type
        :return: The newly created employee type
        :raises HTTPException: When an error occurs during the creation of the employee type
        """
        try:
            new_employee_type = EmployeeTypeServices.create_employee_type(employee_type)
            return new_employee_type

        except EmployeeTypeExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_type_by_id(employee_type_id: str):
        """
        Get an employee type with the given id

        :param employee_type_id: The id of the employee type to retrieve
        :return: The employee type with the given id
        :raises HTTPException: When the employee type is not found or when an error occurs during retrieval
        """
        try:
            employee_type = EmployeeTypeServices.get_employee_type_by_id(employee_type_id)
            if employee_type:
                return employee_type
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_type_by_type_name(employee_type_name: str):
        """
        Get an employee type with the given type name

        :param employee_type_name: The name of the employee type to retrieve
        :return: The employee type with the given name
        :raises HTTPException: When the employee type is not found or when an error occurs during retrieval
        """
        try:
            employee_type = EmployeeTypeServices.get_employee_type_by_id(employee_type_name)
            if employee_type:
                return employee_type
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_employee_types():
        """
        Get all employee types

        :return: A list of all employee types
        """
        employee_types = EmployeeTypeServices.get_all_employee_types()
        return employee_types

    @staticmethod
    def delete_employee_type_by_id(employee_type_id: str):
        try:
            EmployeeTypeServices.delete_employee_type_by_id(employee_type_id)
            return Response(content=f"Employee type with id - {employee_type_id} is deleted")
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_employee_type(employee_type_id: str, employee_type: str):
        """
         Update an employee type with the given id

        :param employee_type_id: The id of the employee type to update
        :param employee_type: The new name for the employee type
        :return: The updated employee type
        :raises HTTPException: When the employee type is not found or when an error occurs during update
        """
        try:
            e_type = EmployeeTypeServices.update_employee_type(employee_type_id, employee_type)
            return e_type
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
