from app.db.database import SessionLocal
from app.products.repositories import LineRepository


class LineServices:
    @staticmethod
    def create_new_line(brand: str, model: str, length: int, AFTM: str, price: int,
                        quantity: int, description: str, in_stock: bool, product_id: str, product_type_id: str):
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.create_new_line(brand=brand, model=model, length=length,
                                                       AFTM=AFTM, price=price, quantity=quantity,
                                                       description=description, in_stock=in_stock,
                                                       product_id=product_id, product_type_id=product_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_line_by_id(line_id: str):
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.get_line_by_id(line_id=line_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_lines_by_brand_name(brand: str):
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.get_lines_by_brand_name(brand=brand)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_lines():
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.get_all_lines()
        except Exception as e:
            raise e

    @staticmethod
    def delete_line_by_id(line_id: str):
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                line_repository.delete_line_by_id(line_id=line_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_line(line_id: str, brand: str = None, model: str = None, length: int = None,
                    AFTM: str = None, price: int = None, quantity: int = None,
                    description: str = None, in_stock: bool = None, product_id: str = None,
                    product_type_id: str = None):
        try:
            with SessionLocal() as db:
                line_repository = LineRepository(db)
                return line_repository.update_line(line_id=line_id, brand=brand, model=model, length=length,
                                                   AFTM=AFTM, price=price, quantity=quantity,
                                                   description=description, in_stock=in_stock, product_id=product_id,
                                                   product_type_id=product_type_id)
        except Exception as e:
            raise e
