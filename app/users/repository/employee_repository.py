from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import Optional

from app.users.exceptions import *
from app.users.models import Employee, User


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: str):
        user = self.db.query(User).filter(User.user_id == user_id).first()
        return user

    def create_employee(self, user_id, employee_type_id):
        """Create a new employee in the database.

        :param first_name: The first name of the employee
        :param last_name: The last name of the employee
        :param employee_type_id: The employee type ID of the employee
        :param user_id: The user ID of the employee

        :return: The created Employee instance
        :raises: IntegrityError: If there is a conflict in the database while creating the employee"""
        try:
            user = self.get_user(user_id)
            employee = Employee(first_name=user.first_name, last_name=user.last_name, user_id=user_id,
                                employee_type_id=employee_type_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def get_employee_by_id(self, employee_id: str):
        """Get an employee by their ID.

        :param employee_id: The ID of the employee to retrieve

        :return: The retrieved Employee instance
        :raises: EmployeeNotFoundException: If no employee is found with the given ID"""
        employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(f"Employee with provided ID: {employee_id} not found.", 400)
        return employee

    def get_employees_by_first_name(self, first_name: str):
        """Get employees by their first name.

        :param first_name: The first name of the employees to retrieve.
        :return: A list of Employee instances
        :raises: EmployeeNotFoundException: If no employees are found with the given first name"""
        employees = self.db.query(Employee).filter(Employee.first_name.like(first_name + "%")).all()
        if employees is None:
            raise EmployeeNotFoundException(f"Employee with provided name: {first_name} not found.", 400)
        return employees

    def get_employees_by_employee_type_id(self, employee_type_id: str):
        """Get employees by their employee type ID.

        :param employee_type_id: The employee type ID of the employees to retrieve
        :return: A list of Employee instances
        :raises: EmployeeNotFoundException: If no employees are found with the given employee type ID"""
        employees = self.db.query(Employee).filter(Employee.employee_type_id == employee_type_id).all()
        if employees is None:
            raise EmployeeNotFoundException(
                f"Employee with provided employee type id: {employee_type_id} not found.",
                400,
            )
        return employees

    def get_all_employees(self):
        """Get all employees in the database.

        :return: A list of all Employee instances"""
        employees = self.db.query(Employee).all()
        return employees

    def delete_employee_by_id(self, employee_id: str):
        """Deletes an employee by ID.

        :return: True if the employee was deleted successfully, False otherwise."""
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided ID: {employee_id} not found.", 400)
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee(self, employee_id: str, first_name: str = None,
                        last_name: str = None, user_id: str = None, employee_type_id: str = None):
        """Update an employee by their ID.

        :param employee_id: The ID of the employee to update
        :param first_name: (Optional) The updated first name of the employee
        :param last_name: (Optional) The updated last name of the employee
        :param employee_type_id: (Optional) The updated employee type ID of the employee
        :param user_id: (Optional) The updated user ID of the employee

        :return: The updated Employee instance
        :raises: EmployeeNotFoundException: If no employee is found with the given ID"""
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided ID: {employee_id} not found.", 400)
            if first_name is not None:
                employee.first_name = first_name
            if last_name is not None:
                employee.last_name = last_name
            if user_id is not None:
                employee.user_id = user_id
            if employee_type_id is not None:
                employee.employee_type_id = employee_type_id
            self.db.add(employee)

            if user_id is not None:
                user = self.get_user(user_id)
                if user is None:
                    raise UserNotFoundException(f"User with provided ID: {user_id} not found.", 400)
                if first_name is not None:
                    user.first_name = first_name
                if last_name is not None:
                    user.last_name = last_name
                self.db.add(user)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e
