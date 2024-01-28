from domain import orders as domain_order
from message import orders as message_order

from fastapi import APIRouter, Query, Header, Request, Form
from fastapi.responses import JSONResponse
from typing import Optional, List

router = APIRouter()

@router.get(
    path="/get-products/",
    response_model=message_order.GetProductsResponseModel,
    summary="Get all products.",
    tags=["products"]
)
def get_products(limit: Optional[int] = 0, offset: Optional[int] = 0, include_out_of_stock: bool = False):
    r = domain_order.get_products(limit=limit, offset=offset, include_out_of_stock=include_out_of_stock)
    return r


@router.post(
    path="/place-order/",
    response_model=str,
    summary="Get all products.",
    tags=["Orders"]
)
def place_order(msg: message_order.PlaceOrderModel):
    msg = msg.dict()
    result = domain_order.place_order(**msg)
    return result