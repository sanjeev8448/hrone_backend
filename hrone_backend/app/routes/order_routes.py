from fastapi import APIRouter
from app.models.order_model import OrderModel
from app.db import orders_collection
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: OrderModel):
    result = await orders_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id), **order.dict()}

@router.get("/orders/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = orders_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = []
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        doc.pop("_id")
        orders.append(doc)
    return orders
