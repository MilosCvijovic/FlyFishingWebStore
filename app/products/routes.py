from fastapi import APIRouter, Depends

from app.products.controller.product_controller import ProductController
from app.products.schemas import *

product_router = APIRouter(tags=["products"], prefix="/api/products")


@product_router.post("/add-new-product", response_model=ProductSchema)
def create_user(product: ProductSchemaIn):
    return ProductController.create_product(product.name, product.price, product.quantity, product.description)


@product_router.get("/id", response_model=ProductSchema)
def get_product_by_id(product_id: str):
    return ProductController.get_product_by_id(product_id)


@product_router.get("/get-all-products", response_model=ProductSchema)
def get_all_products():
    return ProductController.get_all_product()


@product_router.put("/update-product", response_model=ProductSchema)
def update_product(product_id: str, name: str, price: float, quantity: int, description: str):
    return ProductController.update_product(product_id=product_id, name=name, price=price,
                                            quantity=quantity, description=description)


@product_router.delete("/")
def delete_product_by_id(product_id: str):
    return ProductController.delete_product_by_id(product_id=product_id)
