from pydantic import BaseModel
from typing import Optional

class ProductModel(BaseModel):
    name: str
    price: float
    size: Optional[str] = None
    description: Optional[str] = None
