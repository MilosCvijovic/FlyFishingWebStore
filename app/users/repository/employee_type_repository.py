from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import EmployeeType
from app.users.exceptions import *


class EmployeeTypeRepository:
    """This class contains methods to interact with the 'employee type' table in the database."""
    def __init__(self, db: Session):
        """Initialize the EmployeeTypeRepository with a database session
        :param db: a SQLAlchemy Session object"""
        self.db = db

    def create_employee_type(self, employee_type: str):
        """Create a new employee type in the database.

        :param employee_type: string representing the type of the employee
        :return: the created employee type object
        :raises IntegrityError: if the provided employee type already exists in the database"""
        try:
            new_employee_type = EmployeeType(employee_type=employee_type)
            self.db.add(new_employee_type)
            self.db.commit()
            self.db.refresh(new_employee_type)
            return new_employee_type
        except IntegrityError as e:
            raise e

    def read_employee_type_by_id(self, employee_type_id: str):
        """Retrieve an employee type from the database by ID.

        :param employee_type_id: string representing ID of the employee type
        :return: the employee type object
        :raises EmployeeTypeNotFoundException: if the provided employee type ID does not exist in the database"""
        employee_type = self.db.query(EmployeeType).filter(EmployeeType.employee_type_id == employee_type_id).first()
        if employee_type is None:
            raise EmployeeTypeNotFoundException(f"Employee type with provided ID: {employee_type_id} not found.", 400)
        return employee_type

    def read_employee_type_by_type(self, employee_type: str):
        """ Retrieve an employee type from the database by type.

        :param employee_type: string representing the type of the employee type
        :return: the employee type object"""
        read_employee_type = self.db.query(EmployeeType).filter(EmployeeType.employee_type == employee_type).first()
        return read_employee_type

    def read_all_employee_types(self):
        """Retrieve all employee types from the database.

        :return: list of employee type objects"""
        employee_types = self.db.query(EmployeeType).all()
        return employee_types

    def delete_employee_type_by_id(self, employee_type_id: str):
        """Delete an employee type from the database by ID.

        :param employee_type_id: string representing ID of the employee type
        :return: True if the employee type was successfully deleted
        :raises EmployeeTypeNotFoundException: if the provided employee type ID does not exist in the database
        :raises Exception: if any other error occurs"""
        try:
            employee_type = self.db.query(EmployeeType).filter(
                EmployeeType.employee_type_id == employee_type_id).first()
            if employee_type is None:
                raise EmployeeTypeNotFoundException(f"Employee type with provided ID: "
                                                    f"{employee_type_id} not found.", 400)
            self.db.delete(employee_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee_type(self, employee_type_id: str, employee_type: str):
        """Updates the employee type in the database with the given ID.

        :param employee_type_id: string representing the ID of the employee type to be updated.
        :param employee_type: string representing the updated type of the employee.
        :return: EmployeeType object representing the updated employee type.
        :raises: Exception if there was an error updating the employee type in the database.
                 EmployeeTypeNotFoundException if no employee type with the given ID was found."""
        try:
            employee_type_update = self.db.query(EmployeeType).filter(
                EmployeeType.employee_type_id == employee_type_id).first()
            if employee_type_update is None:
                raise EmployeeTypeNotFoundException(f"Employee type with provided ID: "
                                                    f"{employee_type_id} not found.", 400)
            employee_type_update.employee_type = employee_type
            self.db.add(employee_type_update)
            self.db.commit()
            self.db.refresh(employee_type_update)
            return employee_type_update
        except Exception as e:
            raise e
