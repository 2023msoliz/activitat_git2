from typing import Union
import product_db
from fastapi import FastAPI
import models
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/product/")
def get_products():
    data=product_db.read()
    return {"products": data}


@app.get("/product/{id}")
def get_products(id: int,):
    data=product_db.readId(id)
    return {"product": data}

@app.post("/products")
def createProduct(product: models.PostProduct):
    product=product_db.createproduct(product)
    return {"product": product}


@app.put("/products/{id}")
def updateProduct(id: int, product: models.PostProduct):
    updated_product = product_db.updateProducts(id, product)
    return {"product": updated_product}

