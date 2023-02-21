import pytest

from app.products.repositories import ProductRepository
from app.tests import TestClass, TestingSessionLocal


class TestProductRepo(TestClass):
    def test_create_product(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)
            assert product.brand == "Shimano"
            assert product.model == "Biocraft XR"
            assert product.price == 1500

    def test_create_product_error(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)
            assert not product.brand != "Shimano"
            assert not product.model != "Biocraft XR"
            assert not product.price != 1500

    def test_get_product_by_id(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)

            product_id = product_repository.get_product_by_id(product.product_id)

            assert product.product_id == product_id.product_id

    def test_get_product_by_id_error(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)

            product_id = product_repository.get_product_by_id(product.product_id)

            assert not product.product_id != product_id.product_id

    def test_get_product_by_brand_name(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)
            product = product_repository.create_new_product("Shimano", "Biocraft XTC", 1500)

            brand_name = product_repository.get_products_by_brand_name("Shimano")

            assert len(brand_name) == 2

    def test_get_product_by_brand_name_error(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)
            product = product_repository.create_new_product("Shimano", "Biocraft XTC", 1500)

            brand_name = product_repository.get_products_by_brand_name("Shimano")

            assert not len(brand_name) != 2

    def test_get_all_products(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)
            product = product_repository.create_new_product("Shimano", "Biocraft XTC", 1500)

            products = product_repository.get_all_products()

            assert len(products) == 2

    def test_get_all_products_error(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)
            product = product_repository.create_new_product("Shimano", "Biocraft XTC", 1500)

            products = product_repository.get_all_products()

            assert not len(products) != 2

    def test_delete_product_by_id(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)

            assert product_repository.delete_product_by_id(product.product_id) is True

    def test_delete_product_by_id_error(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)

            assert not product_repository.delete_product_by_id(product.product_id) is False

    def test_update_product(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)

            update_product = product_repository.update_product(product.product_id, "Shimano", "Biocraft XTC", 1200)

            assert product.product_id == update_product.product_id
            assert product.brand == update_product.brand
            assert product.model == update_product.model
            assert product.price == update_product.price

    def test_update_product_error(self):
        with TestingSessionLocal() as db:
            product_repository = ProductRepository(db)

            product = product_repository.create_new_product("Shimano", "Biocraft XR", 1500)

            update_product = product_repository.update_product(product.product_id, "Shimano", "Biocraft XTC", 1200)

            assert not product.product_id != update_product.product_id
            assert not product.brand != update_product.brand
            assert not product.model != update_product.model
            assert not product.price != update_product.price
