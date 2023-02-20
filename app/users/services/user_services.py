import codecs

import hashlib
from app.config import settings
from app.users.repository.user_repository import UserRepository
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword


class UserServices:

    @staticmethod
    def create_user(first_name: str, last_name: str, email: str, telephone_number: str, password: str, address: str):
        """Creates a new user with the specified name, email, password and address.

        :param first_name: Name of the user.
        :param last_name: Last name of the user.
        :param email: email address of the user
        :param telephone_number: telephone_number of the user
        :param password: password of the user
        :param address: address of the user
        :return: newly created user
        :raises: Exception"""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(first_name=first_name, last_name=last_name, email=email,
                                                   telephone_number=telephone_number, password=hashed_password,
                                                   address=address)
            except Exception as e:
                raise e

    @staticmethod
    def create_super_user(first_name: str, last_name: str, email: str, telephone_number: str,
                          password: str, address: str):
        """Creates a new superuser with the specified name, email, password and address.

        :param first_name: Name of the user.
        :param last_name: Last name of the user.
        :param email: email address of the user
        :param telephone_number: telephone_number of the user
        :param password: password of the user
        :param address: address of the user
        :return: newly created superuser
        :raises: Exception"""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(first_name=first_name, last_name=last_name, email=email,
                                                         telephone_number=telephone_number,
                                                         password=hashed_password, address=address)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
        """Logs user with the specified email and password.

        :param email: email address of the user
        :param password: password of the user
        :return: user that is logged in
        :raises: UserInvalidPassword, Exception"""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """Updates the is_active attribute of the user with the specified user_id.

        :param user_id: id of the user to be updated
        :param is_active: new value for the is_active attribute
        :return: the updated user
        :raises: Exception"""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id=user_id, is_active=is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_user_is_super_user(user_id: str, is_superuser: bool):
        """ Updates the is_superuser attribute of the user with the specified user_id.

        :param user_id: id of the user to be updated
        :param is_superuser: new value for the is_superuser attribute
        :return: the updated user
        :raises: Exception"""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_super_user(user_id=user_id, is_superuser=is_superuser)
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        """Gets the user with the specified user_id.

        :param user_id: id of the user to be retrieved
        :return: the user with the specified user_id"""
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_user_by_id(user_id)

    @staticmethod
    def get_all_users():
        """ Gets all users.

        :return: list of all users"""
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def delete_user_by_id(user_id: str):
        """ Deletes a user from the database based on the provided user id.

        :param: user_id The id of the user to be deleted.
        :raises:  Exception: If any error occurs while trying to delete the user."""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e
