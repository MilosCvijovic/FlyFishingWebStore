from app.db.database import Base
from sqlalchemy import Column, String, Integer, Float
from uuid import uuid4


class ProductType(Base):
    __tablename__ = "product_types"
    product_type_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    product_type = Column(String(50))

    def __init__(self, product_type):
        self.product_type = product_type
