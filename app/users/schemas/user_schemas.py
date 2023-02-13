from pydantic import BaseModel
from pydantic import UUID4, EmailStr


class UserSchema(BaseModel):
    """UserSchema model defines the structure of a User data.

    :param user_id: Unique identifier for the user.
    :param name: Name of the user.
    :param email: Email address of the user.
    :param telephone_number: Telephone_number of the user.
    :param password: Password of the user.
    :param address: Address of the user.
    :param is_active: Indicates if the user is active.
    :param is_superuser: Indicates if the user has superuser privileges."""
    user_id: UUID4
    name: str
    email: EmailStr
    telephone_number: str
    password: str
    address: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    """UserSchemaIn model defines the structure of a User data for input.

    :param name: Name of the user.
    :param email: Email address of the user.
    :param telephone_number: Telephone_number of the user.
    :param password: Password of the user.
    :param address: Address of the user."""
    name: str
    email: EmailStr
    telephone_number: str
    password: str
    address: str

    class Config:
        orm_mode = True


class UserSchemaLogIn(BaseModel):
    """UserSchemaIn model defines the structure of a User data for log in input.

    :param email: Email address of the user.
    :param password: Password of the user."""
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
