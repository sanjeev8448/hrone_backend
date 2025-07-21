from fastapi import APIRouter, Query
from typing import Optional
from app.models.product_model import ProductModel
from app.db import products_collection
from bson import ObjectId
import re

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductModel):
    result = await products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id), **product.dict()}

@router.get("/products")
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["size"] = size

    cursor = products_collection.find(query).skip(offset).limit(limit)
    products = []
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        doc.pop("_id")
        products.append(doc)
    return products
