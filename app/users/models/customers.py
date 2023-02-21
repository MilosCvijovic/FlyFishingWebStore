from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Customer(Base):
    """The Customer class represents a customer in the database.

    :param first_name: The first name of the customer.
    :param last_name: The last name of the customer.
    :param user_id: The ID of the user associated with the customer."""
    __tablename__ = "customers"
    customer_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    first_name = Column(String(100))
    last_name = Column(String(100))

    user_id = Column(String(50), ForeignKey("users.user_id"))
    user = relationship("User", lazy="subquery")

    def __init__(self, first_name, last_name, user_id):
        """
        Initialize a new instance of the Customer class.

        :param first_name: The first name of the customer.
        :param last_name: The last name of the customer.
        :param user_id: The ID of the user associated with the customer."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    def __eq__(self, other):
        if self.first_name != other.first_name:
            return False
        if self.last_name != other.last_name:
            return False
        if self.user_id != other.user_id:
            return False
        return True

    def __ne__(self, other):
        if self.first_name == other.first_name:
            return False
        if self.last_name == other.last_name:
            return False
        if self.user_id == other.user_id:
            return False
        return True
