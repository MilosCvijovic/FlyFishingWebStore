from fastapi import APIRouter, Depends
from app.users.controller import UserController, EmployeeTypeController, EmployeeController, CustomerController
from app.users.schemas import *
from app.users.controller.user_auth_controller import JWTBearer


user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.name, user.email, user.telephone_number, user.password, user.address)


@user_router.post("/add-new-super-user", response_model=UserSchema)
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.name, user.email, user.telephone_number, user.password, user.address)


@user_router.post("/login")
def login_user(user: UserSchemaLogIn):
    return UserController.login_user(user.email, user.password)


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user_is_active(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id=user_id, is_active=is_active)


@user_router.put("/update/is_superuser", response_model=UserSchema)
def update_user_is_super_user(user_id: str, is_superuser: bool):
    is_superuser = True if is_superuser == 1 else False
    return UserController.update_user_is_super_user(user_id=user_id, is_superuser=is_superuser)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


employee_type_router = APIRouter(tags=["employee-type"], prefix="/api/employee-type")


@employee_type_router.post("/add-new-employee-type", response_model=EmployeeTypeSchema)
def create_employee_type(employee_type: EmployeeTypeSchemaIn):
    return EmployeeTypeController.create_employee_type(employee_type.employee_type)


@employee_type_router.get("/id", response_model=EmployeeTypeSchema)
def get_employee_type_by_id(employee_type_id: str):
    return EmployeeTypeController.get_employee_type_by_id(employee_type_id)


@employee_type_router.get("/get-all-employee-types", response_model=list[EmployeeTypeSchema])
def get_all_employee_types():
    return EmployeeTypeController.get_all_employee_types()


@employee_type_router.delete("/")
def delete_employee_type_by_id(employee_type_id: str):
    return EmployeeTypeController.delete_employee_type_by_id(employee_type_id)


@employee_type_router.put("/update", response_model=EmployeeTypeSchema)
def update_employee_type(employee_type_id, employee_type):
    return EmployeeTypeController.update_employee_type(employee_type_id, employee_type)


employee_router = APIRouter(tags=["employee"], prefix="/api/employees")


@employee_router.post("/add-new-employee", response_model=EmployeeSchema,
                      dependencies=[Depends(JWTBearer("super_user"))])
def create_employee(employee: EmployeeSchemaIn):
    return EmployeeController.create_employee(employee.first_name, employee.last_name, employee.user_id,
                                              employee.employee_type_id)


@employee_router.get("/id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str):
    return EmployeeController.get_employee_by_id(employee_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    return EmployeeController.get_all_employees()


@employee_router.get("/get-employees-by-first-name", response_model=list[EmployeeSchema])
def get_employees_by_first_name(first_name):
    return EmployeeController.get_employees_by_first_name(first_name)


@employee_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_employee_by_id(employee_id: str):
    return EmployeeController.delete_employee_by_id(employee_id)


@employee_router.put("/update-employee-by-id", response_model=EmployeeSchema,
                     dependencies=[Depends(JWTBearer("super_user"))])
def update_employee(employee_id: str, first_name: str = None, last_name: str = None, user_id: str = None,
                    employee_type_id: str = None):
    return EmployeeController.update_employee(employee_id, first_name, last_name, user_id, employee_type_id)


customer_router = APIRouter(tags=["customer"], prefix="/api/customers")


@customer_router.post("/add-new-customer", response_model=CustomerSchema)
def create_customer(customer: CustomerSchemaIn):
    return CustomerController.create_customer(customer.first_name, customer.last_name, customer.user_id)


@customer_router.get("/id", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str):
    return CustomerController.get_customer_by_id(customer_id)


@customer_router.get("/get-all-customers", response_model=list[CustomerSchema])
def get_all_customers():
    return CustomerController.get_all_customers()


@customer_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_customer_by_id(customer_id: str):
    return CustomerController.delete_customer_by_id(customer_id)


@customer_router.put("/update-customer-by-id", response_model=CustomerSchema,
                     dependencies=[Depends(JWTBearer("super_user"))])
def update_employee(customer_id: str, name: str = None, last_name: str = None, user_id: str = None):
    return CustomerController.update_customer(customer_id, name, last_name, user_id)
