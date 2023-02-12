from pydantic import UUID4, BaseModel, EmailStr
from app.users.schemas.user_schemas import UserSchema


class CustomerSchema(BaseModel):
    """Model to represent the customer data.

    :param customer_id: Unique identifier for the customer.
    :param first_name: First name of the customer.
    :param last_name: Last name of the customer.
    :param user_id: Foreign key reference to the User model.
    :param user: Instance of the User model."""
    customer_id: UUID4
    first_name: str
    last_name: str
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    """Model to represent the input data to create a customer.

    :param first_name: First name of the customer.
    :param last_name: Last name of the customer.
    :param user_id: Foreign key reference to the User model."""
    first_name: str
    last_name: str
    user_id: str

    class Config:
        orm_mode = True
