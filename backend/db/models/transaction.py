from sqlalchemy.orm import Mapped
from .. import Base


class Transaction(Base):
    __tablename__ = "transactions"

    owner: Mapped[str]
    amount: Mapped[str]
    date: Mapped[str]
    description: Mapped[str]
    category: Mapped[str]