import pytest

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import EmployeeTypeRepository


class TestEmployeeTypeRepo(TestClass):
    def create_employee_types_for_methods(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type = employee_type_repository.create_employee_type("prodavac")

    def test_create_employee_type(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            em_id = employee_type_repository.read_employee_type_by_id(employee_type_id=employee_type1.employee_type_id)

            assert em_id.employee_type_id == employee_type1.employee_type_id
            assert em_id.employee_type == "prodavac"

    def test_create_employee_type_error(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            em_id = employee_type_repository.read_employee_type_by_id(employee_type_id=employee_type1.employee_type_id)

            assert not em_id.employee_type_id != employee_type1.employee_type_id
            assert not em_id.employee_type != "prodavac"

    def test_get_employee_type_by_id(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            em_id = employee_type_repository.read_employee_type_by_id(employee_type_id=employee_type1.employee_type_id)

            assert em_id.employee_type_id == employee_type1.employee_type_id

    def test_get_employee_type_by_id_error(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            em_id = employee_type_repository.read_employee_type_by_id(employee_type_id=employee_type1.employee_type_id)

            assert not em_id.employee_type_id != employee_type1.employee_type_id

    def test_get_employee_type_by_type(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            em_type = employee_type_repository.read_employee_type_by_type(employee_type=employee_type1.employee_type)

            assert em_type.employee_type == employee_type1.employee_type

    def test_get_employee_type_by_type_error(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")
            em_type = employee_type_repository.read_employee_type_by_type(employee_type=employee_type1.employee_type)

            assert not em_type.employee_type != employee_type1.employee_type

    def test_get_all_employee_types(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            self.create_employee_types_for_methods()

            em_type = employee_type_repository.read_all_employee_types()

            assert len(em_type) == 1

    def test_get_all_employee_types_error(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            self.create_employee_types_for_methods()

            em_type = employee_type_repository.read_all_employee_types()

            assert not len(em_type) != 1

    def test_delete_employee_type(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")

            assert employee_type_repository.delete_employee_type_by_id(employee_type_id=employee_type1.employee_type_id) is True

    def test_delete_employee_type_error(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")

            assert not employee_type_repository.delete_employee_type_by_id(employee_type_id=employee_type1.employee_type_id) is False

    def test_update_employee_type(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")

            employee = employee_type_repository.update_employee_type(employee_type_id=employee_type1.employee_type_id, employee_type="kasir")

            assert employee_type1.employee_type == employee.employee_type
            assert employee_type1.employee_type_id == employee.employee_type_id

    def test_update_employee_type_error(self):
        with TestingSessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            employee_type1 = employee_type_repository.create_employee_type("prodavac")

            employee = employee_type_repository.update_employee_type(employee_type_id=employee_type1.employee_type_id,
                                                                     employee_type="kasir")

            assert not employee_type1.employee_type != employee.employee_type
            assert not employee_type1.employee_type_id != employee.employee_type_id
