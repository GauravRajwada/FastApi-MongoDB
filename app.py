from typing import Union

from fastapi import FastAPI

from views.orders import router as order_router


app_params = {
    "description": "Cosmocloud Ecommerce Api",
    "title": "Cosmocloud",
    "docs_url": "/swagger"
}

app = FastAPI(**app_params)

@app.get("/")
def read_root():
    return {"Welcome to Cosmocloud Ecommerce"}

url_prefix = "/api"

app.include_router(order_router, prefix=url_prefix)


