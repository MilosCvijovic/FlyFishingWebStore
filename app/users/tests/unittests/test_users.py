import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import UserRepository


class TestUserRepo(TestClass):
    def create_users_for_methods(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos2@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos3@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos4@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")

    def test_create_user(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="milos1@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")
            assert user.email == "milos1@gmail.com"
            assert user.is_superuser is False
            assert user.is_active is True

    def test_create_user_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Misa", last_name="Misic", email="misa@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")
            assert user.is_active is not False
            with pytest.raises(IntegrityError) as e:
                user1 = user_repository.create_user(first_name="Misa", last_name="Misic", email="misa@gmail.com", telephone_number="123123123", password="sifra123", address="asdasda 11")

    def test_create_super_user(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            assert super_user.email == "milos@gmail.com"
            assert super_user.is_superuser is True

    def test_create_super_user_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            assert super_user.is_superuser is not False
            with pytest.raises(IntegrityError) as e:
                user1 = user_repository.create_super_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")

    def test_get_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            user1 = user_repository.get_user_by_id(user_id=user.user_id)
            assert user == user1

    def test_get_user_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            user1 = user_repository.get_user_by_id(user_id=user.user_id)
            assert not user != user1

    def test_get_all_users(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert len(all_users) == 4

    def test_get_all_users_error(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert not len(all_users) != 4

    def test_delete_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            assert user_repository.delete_user_by_id(user.user_id) is True

    def test_delete_user_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            assert user_repository.delete_user_by_id(user.user_id) is not False

    def test_update_user_is_active(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            user = user_repository.update_user_is_active(user.user_id, False)
            assert user.is_active is False

    def test_update_user_is_active_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            user = user_repository.update_user_is_active(user.user_id, False)
            assert user.is_active is not True

    def test_read_user_by_email(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            assert user.email == "milos@gmail.com"

    def test_read_user_by_email_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(first_name="Milos", last_name="Misic", email="milos@gmail.com", telephone_number="123123123", password="sifra1253", address="asdasda 11")
            assert not user.email != "milos@gmail.com"
