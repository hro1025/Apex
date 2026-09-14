from sqlalchemy import select

from database.db import get_session
from models.account import Account


def get_all_accounts() -> list[Account]:
    with get_session() as session:
        return list(session.scalars(select(Account)))


def create_account(name: str, category: str, balance: float) -> None:
    with get_session() as session:
        account = Account(name=name, category=category, balance=balance)
        session.add(account)
        session.commit()
