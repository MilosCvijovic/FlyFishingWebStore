import pytest

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import UserRepository, CustomerRepository


class TestCustomerRepo(TestClass):
    def create_customers_for_methods(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")

            customer1 = customer_repository.create_customer(user.user_id)
            customer1 = customer_repository.create_customer(user.user_id)
            customer1 = customer_repository.create_customer(user.user_id)
            customer1 = customer_repository.create_customer(user.user_id)

    def test_create_customer(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            customer1 = customer_repository.create_customer(user.user_id)

            assert customer1.first_name == "Misa"
            assert customer1.last_name == "Misic"
            assert customer1.user_id == user.user_id

    def test_create_customer_error(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            customer1 = customer_repository.create_customer(user.user_id)
            assert not customer1.first_name != "Misa"
            assert not customer1.last_name != "Misic"
            assert not customer1.user_id != user.user_id

    def test_get_customer_by_id(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            customer1 = customer_repository.create_customer(user.user_id)
            customer2 = customer_repository.get_customer_by_id(customer1.customer_id)

            assert customer1 == customer2

    def test_get_customer_by_id_error(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)

            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")

            customer1 = customer_repository.create_customer(user.user_id)
            customer2 = customer_repository.get_customer_by_id(customer1.customer_id)

            assert not customer1 != customer2

    def test_get_all_customers(self):
        with TestingSessionLocal() as db:
            self.create_customers_for_methods()
            customer_repository = CustomerRepository(db)

            customers = customer_repository.get_all_customers()

            assert len(customers) == 4

    def test_get_all_customers_error(self):
        with TestingSessionLocal() as db:
            self.create_customers_for_methods()
            customer_repository = CustomerRepository(db)

            customers = customer_repository.get_all_customers()

            assert not len(customers) != 4

    def test_delete_customer_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")
            customer_repository = CustomerRepository(db)
            customer = customer_repository.create_customer(user.user_id)

            assert customer_repository.delete_customer_by_id(customer_id=customer.customer_id) is True

    def test_delete_customer_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")
            customer_repository = CustomerRepository(db)
            customer = customer_repository.create_customer(user.user_id)

            assert customer_repository.delete_customer_by_id(customer_id=customer.customer_id) is not False

    def test_update_customer(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")
            customer_repository = CustomerRepository(db)
            customer = customer_repository.create_customer(user.user_id)
            update_customer = customer_repository.update_customer(customer_id=customer.customer_id, first_name="Milos",
                                                                  last_name="Milosevic", user_id=customer.user_id)
            assert customer.customer_id == update_customer.customer_id
            assert customer.first_name == update_customer.first_name
            assert customer.last_name == update_customer.last_name
            assert customer.user_id == update_customer.user_id

    def test_update_customer_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com",
                                               telephone_number="123123123", password="sifra123", address="asdasda 11")
            customer_repository = CustomerRepository(db)
            customer = customer_repository.create_customer(user.user_id)
            update_customer = customer_repository.update_customer(customer_id=customer.customer_id, first_name="Milos",
                                                                  last_name="Milosevic", user_id=customer.user_id)
            assert not customer.customer_id != update_customer.customer_id
            assert not customer.first_name != update_customer.first_name
            assert not customer.last_name != update_customer.last_name
            assert not customer.user_id != update_customer.user_id
