from pydantic import BaseModel
from typing import Optional

class PostProduct(BaseModel):
    product_id: int
    name: str
    company: str
    price: float
    units: float
    subcategory_id: int
    created_at: str 
    updated_at: str
    

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    company: Optional[str] = None
    price: Optional[float] = None
    units: Optional[int] = None
    subcategory_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
