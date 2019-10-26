from fastapi import FastAPI
from app import products_service
from app.model.dto.product_dto import ProductDto
from app.model.product import Product

api_server = FastAPI()

UPDATE_ONLY_FILLED_FIELDS = True
UPDATE_ALL_FIELDS = False


@api_server.get("/produtos")
def get_all_products():
    products_service.get_products()
    all_products = {}
    return all_products


@api_server.get("/produtos/{product_id}")
def get_product(product_id: str, q: str = None):
    products_service.get_product()
    return {}


@api_server.post("/produtos")
def create_product(product_dto: ProductDto):

    product: Product = ProductDto.parseToProduct()

    products_service.create_product(product)
    return {}


@api_server.put("/produtos/{product_id}")
def update_product(product_id: str, product_dto: ProductDto):

    product: Product = ProductDto.parseToProduct()

    products_service.update_product(product, UPDATE_ALL_FIELDS)
    return {}


@api_server.patch("/produtos/{product_id}")
def patch_product(product_id: str, product_dto: ProductDto):
    product: Product = ProductDto.parseToProduct()

    products_service.update_product(product, UPDATE_ONLY_FILLED_FIELDS)
    return {}


@api_server.delete("/produtos/{product_id}")
def delete_product(product_id: str, q: str = None):
    products_service.delete_product(product_id)
    return {}