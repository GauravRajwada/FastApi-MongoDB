from pydantic import BaseModel
from typing import List, Optional

class ProductsModel(BaseModel):
    ProductId: str
    ProductName: str
    ProductPrice: float
    ProductQuantity: int

class PageModel(BaseModel):
    limit: int
    nextOffSet: Optional[int]
    prevOffSet: Optional[int]
    total: int

class GetProductsResponseModel(BaseModel):
    data: List[ProductsModel]
    page: PageModel

class ItemsModel(BaseModel):
    productId: str
    boughtQuantity: int

class AddressModel(BaseModel):
    city: str
    country: str
    zip_code: str

class PlaceOrderModel(BaseModel):
    items: List[ItemsModel]
    totalAmount: float
    userAddress: AddressModel
