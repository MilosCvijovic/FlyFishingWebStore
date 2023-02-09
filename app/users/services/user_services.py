import codecs

import hashlib
from app.config import settings
from app.users.repository.user_repository import UserRepository
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword


class UserServices:

    @staticmethod
    def create_user(name: str, email: str, password: str, address: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(name=name, email=email, password=hashed_password, address=address)
            except Exception as e:
                raise e

    @staticmethod
    def create_super_user(name: str, email: str, password: str, address: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(name=name, email=email,
                                                         password=hashed_password, address=address)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
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
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id=user_id, is_active=is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_user_is_super_user(user_id: str, is_superuser: bool):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_super_user(user_id=user_id, is_superuser=is_superuser)
            except Exception as e:
                raise e


