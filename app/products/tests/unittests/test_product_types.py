from app.products.repositories import ProductTypeRepository
from app.tests import TestClass, TestingSessionLocal


class TestProductTypeRepo(TestClass):
    def test_create_product(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")
            pr_type = product_type_repository.get_product_type_by_id(product.product_type_id)

            assert pr_type.product_type_id == product.product_type_id
            assert pr_type.product_type == product.product_type

    def test_create_product_error(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")
            pr_type = product_type_repository.get_product_type_by_id(product.product_type_id)

            assert not pr_type.product_type_id != product.product_type_id
            assert not pr_type.product_type != product.product_type

    def test_get_product_type_by_id(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")
            pr_type = product_type_repository.get_product_type_by_id(product.product_type_id)

            assert pr_type.product_type_id == product.product_type_id

    def test_get_product_type_by_id_error(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")
            pr_type = product_type_repository.get_product_type_by_id(product.product_type_id)

            assert not pr_type.product_type_id != product.product_type_id

    def test_get_all_products(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")
            product = product_type_repository.create_product_type("stap")
            product = product_type_repository.create_product_type("struna")

            types = product_type_repository.get_all_product_types()

            assert len(types) == 3

    def test_get_all_products_error(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")
            product = product_type_repository.create_product_type("stap")
            product = product_type_repository.create_product_type("struna")

            types = product_type_repository.get_all_product_types()

            assert not len(types) != 3

    def test_update_product_type(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product_type = product_type_repository.create_product_type(product_type="cekrk")
            update_product = product_type_repository.update_product_type(product_type_id=product_type.product_type_id, product_type="struna")

            assert product_type.product_type == update_product.product_type
            assert product_type.product_type_id == update_product.product_type_id

    def test_update_product_type_error(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type(product_type="cekrk")
            update_product = product_type_repository.update_product_type(product_type_id=product.product_type_id, product_type="struna")

            assert not product.product_type_id != update_product.product_type_id
            assert not product.product_type != update_product.product_type

    def test_delete_product_type(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")

            assert product_type_repository.delete_product_type_by_id(product.product_type_id) is True

    def test_delete_product_type_error(self):
        with TestingSessionLocal() as db:
            product_type_repository = ProductTypeRepository(db)

            product = product_type_repository.create_product_type("cekrk")

            assert not product_type_repository.delete_product_type_by_id(product.product_type_id) is False
