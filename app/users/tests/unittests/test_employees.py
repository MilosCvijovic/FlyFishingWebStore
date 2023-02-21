import pytest

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import EmployeeRepository, EmployeeTypeRepository, UserRepository


class TestEmployeeRepo(TestClass):
    def create_employees_for_methods(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)

    def test_create_employee(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)

            assert employee1.employee_type_id == employee_type1.employee_type_id
            assert employee1.first_name == "Misa"
            assert employee1.last_name == "Misic"

    def test_create_employee_error(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)

            assert not employee1.employee_type_id != employee_type1.employee_type_id
            assert not employee1.first_name != "Misa"
            assert not employee1.last_name != "Misic"

    def test_get_employee_by_id(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)
            employee2 = employee_repository.get_employee_by_id(employee1.employee_id)

            assert employee1 == employee2

    def test_get_employee_by_id_error(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            employee1 = employee_repository.create_employee(user.user_id, employee_type1.employee_type_id)
            employee2 = employee_repository.get_employee_by_id(employee1.employee_id)

            assert not employee1 != employee2

    def test_get_all_employees(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)
            employees = employee_repository.get_all_employees()

            assert len(employees) == 4

    def test_get_all_employees_error(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)
            employees = employee_repository.get_all_employees()

            assert not len(employees) != 4

    def test_get_employees_by_first_name(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)

            employees = employee_repository.get_employees_by_first_name("Misa")

            assert len(employees) == 4

    def test_get_employees_by_first_name_error(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)

            employees = employee_repository.get_employees_by_first_name("Misa")

            assert not len(employees) != 4

    def test_get_employees_by_employee_type(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.read_employee_type_by_type("prodavac")

            employees = employee_repository.get_employees_by_employee_type_id(employee_type1.employee_type_id)

            assert len(employees) == 4

    def test_get_employees_by_employee_type_error(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.read_employee_type_by_type("prodavac")

            employees = employee_repository.get_employees_by_employee_type_id(employee_type1.employee_type_id)

            assert not len(employees) != 4

    def test_delete_employee_by_id(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type = employee_type_repository.create_employee_type("prodavac")
            employee = employee_repository.create_employee(employee_type_id=employee_type.employee_type_id, user_id=user.user_id)
            assert employee_repository.delete_employee_by_id(employee.employee_id) is True

    def test_delete_employee_by_id_error(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type = employee_type_repository.create_employee_type("prodavac")
            employee = employee_repository.create_employee(employee_type_id=employee_type.employee_type_id,
                                                           user_id=user.user_id)
            assert employee_repository.delete_employee_by_id(employee.employee_id) is not False

    def test_update_employee(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type = employee_type_repository.create_employee_type("prodavac")
            employee = employee_repository.create_employee(user.user_id, employee_type.employee_type_id)
            update_employee = employee_repository.update_employee(employee_id=employee.employee_id, first_name="Milos",
                                                                  last_name="Milosevic", user_id=employee.user_id)
            assert employee.employee_id == update_employee.employee_id
            assert employee.first_name == update_employee.first_name
            assert employee.last_name == update_employee.last_name
            assert employee.user_id == update_employee.user_id

    def test_update_employee_error(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            employee_type = employee_type_repository.create_employee_type("prodavac")
            employee = employee_repository.create_employee(user.user_id, employee_type.employee_type_id)
            update_employee = employee_repository.update_employee(employee_id=employee.employee_id, first_name="Milos",
                                                                  last_name="Milosevic", user_id=employee.user_id)
            assert not employee.employee_id != update_employee.employee_id
            assert not employee.first_name != update_employee.first_name
            assert not employee.last_name != update_employee.last_name
            assert not employee.user_id != update_employee.user_id
