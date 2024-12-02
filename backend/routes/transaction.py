from .. import app
from ..schemas import CreateTransaction
from ..db import (SESSION,
                  Transaction
                )

from fastapi import status



@app.post("/create", status_code = status.HTTP_201_CREATED)
def create_transaction(data: CreateTransaction):
    with SESSION.begin() as session:
        transaction = Transaction(**data.model_dump())
        session.add(transaction)
        return transaction