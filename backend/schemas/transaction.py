from typing import Optional

from pydantic import BaseModel, ConfigDict


class CreateTransaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    owner: str
    amount: int
    date: str
    description: str
    category: str
