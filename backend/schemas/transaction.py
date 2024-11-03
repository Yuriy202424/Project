from typing import Optional
from pydantic import BaseModel


class TransactionData(BaseModel):
    id: Optional[int] = None
    owner: str
    amount: str
    date: str
    description: str
    category: str