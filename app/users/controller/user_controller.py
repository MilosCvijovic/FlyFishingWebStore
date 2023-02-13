from sqlalchemy.exc import IntegrityError
from app.users.services import UserServices, signJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidPassword


class UserController:
    """Controller class for User operations.

    This class contains static methods that handle user-related operations."""

    @staticmethod
    def create_user(name: str, email: str, telephone_number: str, password: str, address: str):
        """Create a new user.

        :param name: Name of the user.
        :param email: Email of the user.
        :param telephone_number: Telephone_number of the user.
        :param password: Password of the user.
        :param address: Address of the user.
        :return: The created user.
        :raises HTTPException: In case of any error while creating the user, an HTTPException will be
        raised with a status code and detail message."""
        try:
            user = UserServices.create_user(name=name, email=email, telephone_number=telephone_number,
                                            password=password, address=address)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(name: str, email: str, telephone_number: str, password: str, address: str):
        """Create a new superuser.

        :param name: Name of the user.
        :param email: Email of the user.
        :param telephone_number: Telephone_number of the user.
        :param password: Password of the user.
        :param address: Address of the user.
        :return: The created superuser.
        :raises HTTPException: In case of any error while creating the superuser,
        an HTTPException will be raised with a status code and detail message."""
        try:
            user = UserServices.create_super_user(name=name, email=email, telephone_number=telephone_number,
                                                  password=password, address=address)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email: str, password: str):
        """Login the user.

        :param email: Email of the user.
        :param password: Password of the user.
        :return: The signed JWT token for the user.
        :raises HTTPException: In case of any error while logging in the user,
        an HTTPException will be raised with a status code and detail message."""
        try:
            user = UserServices.login_user(email=email, password=password)
            if user.is_superuser:
                return signJWT(user.user_id, "super_user")
            return signJWT(user.user_id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """Update the active status of a user.

        :param user_id: ID of the user.
        :param is_active: The new active status for the user.
        :return: The updated user.
        :raises HTTPException: In case of any error while updating the user,
        an HTTPException will be raised with a status code and detail message."""
        try:
            return UserServices.update_user_is_active(user_id=user_id, is_active=is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_is_super_user(user_id: str, is_superuser: bool):
        """Update the active status of a user.

        :param user_id: ID of the user.
        :param is_superuser: The new active status for the user.
        :return: The updated user.
        :raises HTTPException: In case of any error while updating the user,
        an HTTPException will be raised with a status code and detail message."""
        try:
            return UserServices.update_user_is_super_user(user_id=user_id, is_superuser=is_superuser)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_id(user_id: str):
        """Get a user by their ID.

        :param user_id: The ID of the user to retrieve.
        :return: The user with the specified ID, if it exists.
        :raises HTTPException: If a user with the specified ID does not exist."""
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"User with provided id: {user_id} does not exist.")

    @staticmethod
    def get_all_users():
        """Get a list of all users.

        :return: A list of all users in the system."""
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        """Delete a user by their ID.

        :param user_id: The ID of the user to delete.
        :return: A response indicating that the user has been deleted.
        :raises HTTPException: If an error occurs while deleting the user."""
        try:
            UserServices.delete_user_by_id(user_id)
            return Response(content=f"User with provided id: {user_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
