from typing import List

from sqlalchemy.exc import IntegrityError
from app.users.services import UserServices, signJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidPassword


class UserController:

    @staticmethod
    def create_user(name: str, email: str, password: str, address: str):
        try:
            user = UserServices.create_user(name=name, email=email, password=password, address=address)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(name: str, email: str, password: str, address: str):
        try:
            user = UserServices.create_super_user(name=name, email=email, password=password, address=address)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email: {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email: str, password: str):
        try:
            user = UserServices.login_user(email=email, password=password)
            if user.is_superuser:
                return signJWT(user.id, "super_user")
            return signJWT(user.id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            return UserServices.update_user_is_active(user_id=user_id, is_active=is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_is_super_user(user_id: str, is_superuser: bool):
        try:
            return UserServices.update_user_is_super_user(user_id=user_id, is_superuser=is_superuser)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


