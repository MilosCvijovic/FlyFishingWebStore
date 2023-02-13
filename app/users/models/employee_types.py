from app.db.database import Base
from sqlalchemy import Column, String
from uuid import uuid4


class EmployeeType(Base):
    """This class represents the 'employee type' table in the database, with attributes
    and methods to interact with the table.

    :param employee_type: string representing the type of the employee.
    """
    __tablename__ = "employee_type"
    employee_type_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    employee_type = Column(String(50), unique=True)

    def __init__(self, employee_type):
        self.employee_type = employee_type
