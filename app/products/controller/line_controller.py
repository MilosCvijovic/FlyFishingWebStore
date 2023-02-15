from fastapi import HTTPException, Response
from app.products.services import LineServices, ProductTypeServices
from app.products.exceptions import *


class LineController:

    @staticmethod
    def create_new_line(brand: str, model: str, length: int, AFTM: str, price: int,
                       quantity: int, description: str, in_stock: bool, product_type_id: str):
        try:
            ProductTypeServices.get_product_type_by_id(product_type_id=product_type_id)
            line = LineServices.create_new_line(brand=brand, model=model, length=length,
                                             AFTM=AFTM, price=price, quantity=quantity,
                                             description=description, in_stock=in_stock,
                                             product_type_id=product_type_id)
            return line
        except ProductTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_line_by_id(line_id: str):
        line = LineServices.get_line_by_id(line_id=line_id)
        if line:
            return line
        raise HTTPException(status_code=400, detail=f"Rod with provided ID: {line_id} is not exist")

    @staticmethod
    def get_line_by_brand_name(brand: str):
        line = LineServices.get_lines_by_brand_name(brand=brand)
        if line:
            return line
        raise HTTPException(status_code=400, detail=f"Rods from this manufacturer: {brand} not found.")

    @staticmethod
    def get_all_lines():
        lines = LineServices.get_all_lines()
        return lines

    @staticmethod
    def delete_line_by_id(line_id: str):
        try:
            LineServices.delete_line_by_id(line_id=line_id)
            return Response(content=f"Rod with provided ID: {line_id} is not exist")
        except LineNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_line(line_id: str, brand: str = None, model: str = None, length: int = None,
                    AFTM: str = None, price: int = None, quantity: int = None,
                   description: str = None, in_stock: bool = None, product_type_id: str = None):
        try:
            return LineServices.update_line(line_id=line_id, brand=brand, model=model, length=length,
                                          AFTM=AFTM, price=price, quantity=quantity,
                                          description=description, in_stock=in_stock,
                                          product_type_id=product_type_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
