from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name: str, email: str, password: str, address: str):
        try:
            user = User(name=name, email=email, password=password, address=address)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, name: str, email: str, password: str, address: str):
        try:
            user = User(name=name, email=email, password=password, address=address, is_superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def read_user_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        return user

    def update_user_is_active(self, user_id: str, is_active: bool):
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
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            user.is_superuser = is_superuser
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

