from pydantic import BaseModel
from typing import List

class OrderModel(BaseModel):
    user_id: str
    products: List[str]  # List of product IDs
