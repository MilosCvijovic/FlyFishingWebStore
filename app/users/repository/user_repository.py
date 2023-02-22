from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User


class UserRepository:
    """This class contains methods to interact with the 'user' table in the database."""
    def __init__(self, db: Session):
        """Initialize the UserRepository with a database session.

        :param db: SQLAlchemy session object."""
        self.db = db

    def create_user(self, first_name: str, last_name: str, email: str, telephone_number: str,
                    password: str, address: str):
        """Create a new User object.

        :param first_name: Name of the user.
        :param last_name: Last name of the user.
        :param email: Email of the user.
        :param telephone_number: Telephone_number of the user.
        :param password: Password of the user.
        :param address: Address of the user.
        :return: The created User object.
        :raises IntegrityError: If the email is already taken."""
        try:
            user = User(first_name=first_name, last_name=last_name, email=email, telephone_number=telephone_number,
                        password=password, address=address)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, first_name: str, last_name: str, email: str, telephone_number: str, password: str,
                          address: str):
        """Create a new User object with superuser privileges.

        :param first_name: Name of the user.
        :param last_name: Last name of the user.
        :param email: Email of the user.
        :param telephone_number: Telephone_number of the user.
        :param password: Password of the user.
        :param address: Address of the user.
        :return: The created User object.
        :raises IntegrityError: If the email is already taken."""
        try:
            user = User(first_name=first_name, last_name=last_name, email=email, telephone_number=telephone_number,
                        password=password, address=address, is_superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def read_user_by_email(self, email: str):
        """Read a User object based on its email.

        :param email: Email of the user.
        :return: The User object, if found. Otherwise, None."""
        user = self.db.query(User).filter(User.email == email).first()
        return user

    def update_user_is_active(self, user_id: str, is_active: bool):
        """Update the "is_active" attribute of a User object.

        :param user_id: ID of the user.
        :param is_active: New value of "is_active".
        :return: The updated User object.
        :raises Exception: If an error occurs during the update process."""
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_user_is_super_user(self, user_id: str, is_superuser: bool):
        """Update the "is_superuser" attribute of a User object.

        :param user_id: ID of the user.
        :param is_superuser: New value of "is_active".
        :return: The updated User object.
        :raises Exception: If an error occurs during the update process."""
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            user.is_superuser = is_superuser
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def get_user_by_id(self, user_id: str):
        """Gets a User by their ID.

        :param user_id: ID of the user.
        :return: The User with specified ID."""
        user = self.db.query(User).filter(User.user_id == user_id).first()
        return user

    def get_all_users(self):
        """Gets all Users.

        :return: A list of all users."""
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id: str):
        """Deletes a User by their ID.

        :param user_id: ID of the user.
        :return: True if delete was successful, False otherwise.
        :raises Exception: If an error occurs during the delete process."""
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e
