from pydantic import BaseModel
from pydantic import UUID4


class EmployeeSchema(BaseModel):
    """Model for the employee data.

    :param id: ID of the employee.
    :param first_name: First name of the employee.
    :param last_name: Last name of the employee.
    :param employee_type_id: ID of the type of employee."""
    employee_id: UUID4
    first_name: str
    last_name: str
    user_id: str
    employee_type_id: str

    class Config:
        orm_mode = True


class EmployeeSchemaIn(BaseModel):
    """Model for the input of employee data.

    :param first_name: Name of the employee.
    :param last_name: Last name of the employee.
    :param employee_type_id: ID of the type of employee."""
    first_name: str
    last_name: str
    user_id: str
    employee_type_id: str

    class Config:
        orm_mode = True
