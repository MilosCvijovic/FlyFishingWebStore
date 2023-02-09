from fastapi import APIRouter, Depends
from app.users.controller import UserController
from app.users.schemas import *
from app.users.controller.user_auth_controller import JWTBearer


user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.name, user.email, user.password, user.address)


@user_router.post("/add-new-super-user", response_model=UserSchema)
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.name, user.email, user.password, user.address)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user_is_active(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id=user_id, is_active=is_active)


@user_router.put("/update/is_superuser", response_model=UserSchema)
def update_user_is_super_user(user_id: str, is_superuser: bool):
    is_superuser = True if is_superuser == 1 else False
    return UserController.update_user_is_super_user(user_id=user_id, is_superuser=is_superuser)

