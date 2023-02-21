from app.db.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4


class User(Base):
    __tablename__ = "users"
    user_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100), unique=True)
    telephone_number = Column(String(50))
    password = Column(String(100))
    address = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __init__(self, first_name, last_name, email, telephone_number, password, address,
                 is_active=True, is_superuser=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone_number = telephone_number
        self.password = password
        self.address = address
        self.is_active = is_active
        self.is_superuser = is_superuser

    def __eq__(self, other):
        if self.user_id != other.user_id:
            return False
        if self.first_name != other.first_name:
            return False
        if self.last_name != other.last_name:
            return False
        if self.email != other.email:
            return False
        if self.telephone_number != other.telephone_number:
            return False
        if self.password != other.password:
            return False
        if self.address != other.address:
            return False
        if self.is_active != other.is_active:
            return False
        if self.is_superuser != other.is_superuser:
            return False
        return True

    def __ne__(self, other):
        if self.user_id == other.user_id:
            return False
        if self.first_name == other.first_name:
            return False
        if self.last_name == other.last_name:
            return False
        if self.email == other.email:
            return False
        if self.telephone_number == other.telephone_number:
            return False
        if self.password == other.password:
            return False
        if self.address == other.address:
            return False
        if self.is_active == other.is_active:
            return False
        if self.is_superuser == other.is_superuser:
            return False
        return True
