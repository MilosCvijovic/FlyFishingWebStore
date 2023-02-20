import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.products.routes import product_type_router, reel_router, rod_router, product_router, line_router, fly_router
from app.shopping_cart.routes import cart_item_router, shopping_cart_router, order_router
from app.users.routes import user_router, employee_type_router, employee_router, customer_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(employee_type_router)
    app.include_router(employee_router)
    app.include_router(customer_router)
    app.include_router(product_type_router)
    app.include_router(product_router)
    app.include_router(rod_router)
    app.include_router(reel_router)
    app.include_router(line_router)
    app.include_router(fly_router)
    app.include_router(cart_item_router)
    app.include_router(shopping_cart_router)
    app.include_router(order_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def first_page():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
