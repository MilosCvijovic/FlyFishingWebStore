from pydantic import BaseModel
from pydantic import UUID4


class EmployeeTypeSchema(BaseModel):
    """Model for storing employee type information

    :param employee_type_id: UUID4 value representing the unique identifier for the employee type
    :param employee_type: String value representing the type of employee"""
    employee_type_id: UUID4
    employee_type: str

    class Config:
        orm_mode = True


class EmployeeTypeSchemaIn(BaseModel):
    """Model for storing employee type information during input/creation

    :param employee_type: String value representing the type of employee"""
    employee_type: str

    class Config:
        orm_mode = True
