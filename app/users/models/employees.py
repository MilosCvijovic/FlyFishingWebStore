from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4


class Employee(Base):
    """This class represents the 'employees' table in the database, with attributes and methods to
    interact with the table.

    :param first_name: String representing first name of the employee
    :param last_name: String representing last name of the employee
    :param employee_type_id: String representing ID of the employee type, foreign key to the 'employee_type' table"""
    __tablename__ = "employees"
    employee_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)

    first_name = Column(String(50))
    last_name = Column(String(50))

    employee_type_id = Column(String(50), ForeignKey("employee_type.employee_type_id"), nullable=False)
    employee_type = relationship("EmployeeType", lazy="subquery")

    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=False)
    user = relationship("User", lazy="subquery")

    def __init__(self, first_name, last_name, user_id, employee_type_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.employee_type_id = employee_type_id
