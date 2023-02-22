from fastapi import APIRouter, Depends

from app.products.controller import RodController, ReelController, LineController, FlyController, ProductController
from app.products.controller.product_type_controller import ProductTypeController
from app.products.schemas import *
from app.users.controller import JWTBearer

product_type_router = APIRouter(tags=["product_types"], prefix="/api/product_types")


@product_type_router.post("/add-new-product_type", response_model=ProductTypeSchema,
                          dependencies=[Depends(JWTBearer("super_user"))])
def create_product_type(product_type: ProductTypeSchemaIn):
    return ProductTypeController.create_product_type(product_type.product_type)


@product_type_router.get("/id", response_model=ProductTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_product_type_by_id(product_type_id: str):
    return ProductTypeController.get_product_type_by_id(product_type_id)


@product_type_router.get("/get-all-product_types", response_model=list[ProductTypeSchema],
                         dependencies=[Depends(JWTBearer("super_user"))])
def get_all_product_types():
    return ProductTypeController.get_all_product_types()


@product_type_router.put("/update-product_type", response_model=ProductTypeSchema,
                         dependencies=[Depends(JWTBearer("super_user"))])
def update_product_type(product_type_id: str, product_type: str):
    return ProductTypeController.update_product_type(product_type_id=product_type_id,
                                                     product_type=product_type)


@product_type_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_product_type_by_id(product_type_id: str):
    return ProductTypeController.delete_product_type_by_id(product_type_id=product_type_id)


product_router = APIRouter(tags=["products"], prefix="/api/products")


@product_router.post("/add-new-product", response_model=ProductSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_product(product: ProductSchemaIn):
    return ProductController.create_new_product(brand=product.brand, model=product.model, price=product.price)


@product_router.get("/id", response_model=ProductSchema)
def get_product_by_id(product_id: str):
    return ProductController.get_product_by_id(product_id)


@product_router.get("/get-all-products", response_model=list[ProductSchema])
def get_all_products():
    return ProductController.get_all_products()


@product_router.put("/update-product", response_model=ProductSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_product(product_id: str, brand: str, model: str, price: int):
    return ProductController.update_product(product_id=product_id, brand=brand, model=model, price=price)


@product_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_product_by_id(product_id: str):
    return ProductController.delete_product_by_id(product_id=product_id)


rod_router = APIRouter(tags=["rod"], prefix="/api/rods")


@rod_router.post("/add-new-rod", response_model=RodSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_new_rod(rod: RodSchemaIn):
    return RodController.create_new_rod(product_type_id=rod.product_type_id, brand=rod.brand, model=rod.model,
                                        length=rod.length, weight=rod.weight, AFTM=rod.AFTM, price=rod.price,
                                        quantity=rod.quantity, description=rod.description, product_id=rod.product_id,
                                        in_stock=rod.in_stock)


@rod_router.get("/id", response_model=RodSchema)
def get_rod_by_id(rod_id: str):
    return RodController.get_rod_by_id(rod_id=rod_id)


@rod_router.get("/brand", response_model=list[RodSchema])
def get_rod_by_brand_name(brand: str):
    return RodController.get_rod_by_brand_name(brand=brand)


@rod_router.get("/get-all-rods", response_model=list[RodSchema])
def get_all_rods():
    return RodController.get_all_rods()


@rod_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_rod_by_id(rod_id: str):
    return RodController.delete_rod_by_id(rod_id=rod_id)


@rod_router.put("/update-rod", response_model=RodSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_rod(rod_id: str, brand: str = None, model: str = None, length: int = None,
               weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
               description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
    return RodController.update_rod(rod_id=rod_id, brand=brand, model=model, length=length,
                                    weight=weight, AFTM=AFTM, price=price, quantity=quantity,
                                    description=description, in_stock=in_stock, product_id=product_id,
                                    product_type_id=product_type_id)


reel_router = APIRouter(tags=["reel"], prefix="/api/reels")


@reel_router.post("/add-new-reel", response_model=ReelSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_new_reel(reel: ReelSchemaIn):
    return ReelController.create_new_reel(product_type_id=reel.product_type_id, product_id=reel.product_id,
                                          brand=reel.brand, model=reel.model,
                                          weight=reel.weight, AFTM=reel.AFTM, price=reel.price,
                                          quantity=reel.quantity, description=reel.description, in_stock=reel.in_stock)


@reel_router.get("/id", response_model=ReelSchema)
def get_reel_by_id(reel_id: str):
    return ReelController.get_reel_by_id(reel_id=reel_id)


@reel_router.get("/brand", response_model=list[ReelSchema])
def get_reel_by_brand_name(brand: str):
    return ReelController.get_reel_by_brand_name(brand=brand)


@reel_router.get("/get-all-reels", response_model=list[ReelSchema])
def get_all_reels():
    return ReelController.get_all_reels()


@reel_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_reel_by_id(reel_id: str):
    return ReelController.delete_reel_by_id(reel_id=reel_id)


@reel_router.put("/update-reel", response_model=ReelSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_reel(reel_id: str, brand: str = None, model: str = None,
                weight: int = None, AFTM: str = None, price: int = None, quantity: int = None,
                description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
    return ReelController.update_reel(reel_id=reel_id, brand=brand, model=model,
                                      weight=weight, AFTM=AFTM, price=price, quantity=quantity,
                                      description=description, in_stock=in_stock, product_id=product_id,
                                      product_type_id=product_type_id)


line_router = APIRouter(tags=["line"], prefix="/api/lines")


@line_router.post("/add-new-line", response_model=LineSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_new_line(line: LineSchemaIn):
    return LineController.create_new_line(product_type_id=line.product_type_id, product_id=line.product_id,
                                          brand=line.brand, model=line.model,
                                          length=line.length, AFTM=line.AFTM, price=line.price,
                                          quantity=line.quantity, description=line.description, in_stock=line.in_stock)


@line_router.get("/id", response_model=LineSchema)
def get_line_by_id(line_id: str):
    return LineController.get_line_by_id(line_id=line_id)


@line_router.get("/brand", response_model=list[LineSchema])
def get_line_by_brand_name(brand: str):
    return LineController.get_line_by_brand_name(brand=brand)


@line_router.get("/get-all-lines", response_model=list[LineSchema])
def get_all_lines():
    return LineController.get_all_lines()


@line_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_line_by_id(line_id: str):
    return LineController.delete_line_by_id(line_id=line_id)


@line_router.put("/update-line", response_model=LineSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_line(line_id: str, brand: str = None, model: str = None, length: int = None,
                AFTM: str = None, price: int = None, quantity: int = None,
                description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
    return LineController.update_line(line_id=line_id, brand=brand, model=model, length=length,
                                      AFTM=AFTM, price=price, quantity=quantity,
                                      description=description, in_stock=in_stock, product_id=product_id,
                                      product_type_id=product_type_id)


fly_router = APIRouter(tags=["fly"], prefix="/api/flies")


@fly_router.post("/add-new-fly", response_model=FlySchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_new_fly(fly: FlySchemaIn):
    return FlyController.create_new_fly(product_type_id=fly.product_type_id, product_id=fly.product_id,
                                        brand=fly.brand, model=fly.model,
                                        length=fly.length, weight=fly.weight, price=fly.price,
                                        quantity=fly.quantity, description=fly.description, in_stock=fly.in_stock)


@fly_router.get("/id", response_model=FlySchema)
def get_fly_by_id(fly_id: str):
    return FlyController.get_fly_by_id(fly_id=fly_id)


@fly_router.get("/brand", response_model=list[FlySchema])
def get_fly_by_brand_name(brand: str):
    return FlyController.get_fly_by_brand_name(brand=brand)


@fly_router.get("/get-all-flies", response_model=list[FlySchema])
def get_all_flies():
    return FlyController.get_all_flies()


@fly_router.delete("/")
def delete_fly_by_id(fly_id: str):
    return FlyController.delete_fly_by_id(fly_id=fly_id)


@fly_router.put("/update-fly", response_model=FlySchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_fly(fly_id: str, brand: str = None, model: str = None, length: int = None,
               weight: int = None, price: int = None, quantity: int = None,
               description: str = None, in_stock: bool = None, product_id: str = None, product_type_id: str = None):
    return FlyController.update_fly(fly_id=fly_id, brand=brand, model=model, length=length,
                                    weight=weight, price=price, quantity=quantity,
                                    description=description, in_stock=in_stock, product_id=product_id,
                                    product_type_id=product_type_id)
