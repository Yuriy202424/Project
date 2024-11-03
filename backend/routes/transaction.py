from .. import app
from ..schemas import TransactionData
from ..db import SESSION, Transaction



@app.post("/create")
def create(data: TransactionData):
    with SESSION.begin() as session:
        transaction = Transaction(**data.model_dump())
        session.add(transaction)
        return transaction