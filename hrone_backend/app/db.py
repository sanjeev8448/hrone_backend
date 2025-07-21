from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URL, DATABASE_NAME

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

products_collection = db["products"]
orders_collection = db["orders"]


