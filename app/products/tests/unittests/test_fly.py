from app.products.repositories import FlyRepository, ProductRepository, ProductTypeRepository
from app.tests import TestClass, TestingSessionLocal


class TestProductTypeRepo(TestClass):
    def test_create_fly(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7, price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            assert product.product_id == fly.product_id
            assert product_type.product_type_id == fly.product_type_id
            assert product.brand == fly.brand
            assert product.price == fly.price

    def test_create_fly_error(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7,
                                                price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            assert not product.product_id != fly.product_id
            assert not product_type.product_type_id != fly.product_type_id
            assert not product.brand != fly.brand
            assert not product.price != fly.price

    def test_get_fly_by_id(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7, price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            fly_id = fly_repository.get_fly_by_id(fly_id=fly.fly_id)

            assert fly_id.fly_id == fly.fly_id

    def test_get_fly_by_id_error(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7, price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            fly_id = fly_repository.get_fly_by_id(fly_id=fly.fly_id)

            assert not fly_id.fly_id != fly.fly_id

    def test_get_fly_by_brand_name(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7, price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            brand_name = fly_repository.get_flies_by_brand_name("domaca radinost")

            assert len(brand_name) == 1

    def test_get_fly_by_brand_name_error(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7, price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            brand_name = fly_repository.get_flies_by_brand_name("domaca radinost")

            assert not len(brand_name) != 1

    def test_get_all_flies(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7, price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            all_flies = fly_repository.get_all_flies()

            assert len(all_flies) == 1

    def test_get_all_flies_error(self):
        with TestingSessionLocal() as db:
            fly_repository = FlyRepository(db)
            product_repository = ProductRepository(db)
            product_type_repository = ProductTypeRepository(db)

            product = product_repository.create_new_product("domaca radinost", "strimer", 700)
            product_type = product_type_repository.create_product_type("musica")

            fly = fly_repository.create_new_fly(brand="domaca radinost", model="strimer", length=9, weight=7, price=700,
                                                quantity=10, description="strimer za stuku", in_stock=True,
                                                product_id=product.product_id,
                                                product_type_id=product_type.product_type_id)

            all_flies = fly_repository.get_all_flies()

            assert not len(all_flies) != 1

