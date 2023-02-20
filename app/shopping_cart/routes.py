from fastapi import APIRouter, Depends
from app.shopping_cart.controller import CartItemController, ShoppingCartController, OrderController
from app.shopping_cart.schemas import *

cart_item_router = APIRouter(tags=["cart_item"], prefix="/api/cart_item")


@cart_item_router.post("/add-new-cart-item", response_model=CartItemSchema)
def create_cart_item(cart_item: CartItemSchemaIn):
    return CartItemController.create_new_cart_item(quantity=cart_item.quantity, product_id=cart_item.product_id, shopping_cart_id=cart_item.shopping_cart_id)


@cart_item_router.get("/id", response_model=CartItemSchema)
def get_cart_item_by_id(cart_id: str):
    return CartItemController.get_cart_item_by_id(cart_id)


@cart_item_router.get("/get-all-cart-items", response_model=list[CartItemSchema])
def get_all_cart_items():
    return CartItemController.get_all_cart_items()


@cart_item_router.put("/update-cart-item", response_model=CartItemSchema)
def update_cart_item(cart_id: str, product_id: str, quantity: int):
    return CartItemController.update_cart_item(cart_id=cart_id, product_id=product_id, quantity=quantity)


@cart_item_router.delete("/")
def delete_cart_item_by_id(cart_id: str):
    return CartItemController.delete_cart_item_by_id(cart_id=cart_id)


shopping_cart_router = APIRouter(tags=["shopping_cart"], prefix="/api/shopping_carts")


@shopping_cart_router.post("/add-new-shopping-cart", response_model=ShoppingCartSchema)
def create_shopping_cart(shopping_cart: ShoppingCartSchemaIn):
    return ShoppingCartController.create_new_shopping_cart(shopping_cart.customer_id)


@shopping_cart_router.get("/id", response_model=ShoppingCartSchemaOut)
def get_shopping_cart_by_id(shopping_cart_id: str):
    return ShoppingCartController.get_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)


@shopping_cart_router.get("/get-all-shopping-carts", response_model=list[ShoppingCartSchemaOut])
def get_all_shopping_carts():
    return ShoppingCartController.get_all_shopping_carts()


@shopping_cart_router.put("/update-shopping-cart", response_model=ShoppingCartSchema)
def update_shopping_cart(shopping_cart_id: str, customer_id: str):
    return ShoppingCartController.update_shopping_cart(shopping_cart_id=shopping_cart_id, customer_id=customer_id)


@shopping_cart_router.delete("/")
def delete_shopping_cart_by_id(shopping_cart_id: str):
    return ShoppingCartController.delete_shopping_cart_by_id(shopping_cart_id=shopping_cart_id)


order_router = APIRouter(tags=["orders"], prefix="/api/orders")


@order_router.post("/add-new-order", response_model=OrderSchema)
def create_new_order(order: OrderSchemaIn):
    return OrderController.create_new_order(shopping_cart_id=order.shopping_cart_id)


@order_router.get("/id", response_model=OrderSchema)
def get_order_by_id(order_id: str):
    return OrderController.get_order_by_id(order_id)


@order_router.get("/get-all-orders", response_model=list[OrderSchema])
def get_all_orders():
    return OrderController.get_all_orders()


@order_router.put("/order-sent", response_model=OrderSchemaOut)
def mark_order_as_sent(order_id: str, shopping_cart_id: str, sent: bool):
    return OrderController.mark_order_as_sent(order_id=order_id, shopping_cart_id=shopping_cart_id, sent=sent)


@cart_item_router.delete("/")
def delete_cart_item_by_id(order_id: str):
    return OrderController.delete_order_by_id(order_id=order_id)
