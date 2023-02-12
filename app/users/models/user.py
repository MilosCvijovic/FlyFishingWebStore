from app.db.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4


class User(Base):
    __tablename__ = "users"
    user_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    telephone_number = Column(String(50))
    password = Column(String(100))
    address = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __init__(self, name, email, telephone_number, password, address, is_active=True, is_superuser=False):
        self.name = name
        self.email = email
        self.telephone_number = telephone_number
        self.password = password
        self.address = address
        self.is_active = is_active
        self.is_superuser = is_superuser
