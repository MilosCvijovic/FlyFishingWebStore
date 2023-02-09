from typing import Optional

from pydantic import BaseModel
from pydantic import UUID4, EmailStr


class UserSchema(BaseModel):
    user_id: UUID4
    name: str
    email: str
    password: str
    address: Optional[str] = None
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str

    class Config:
        orm_mode = True

