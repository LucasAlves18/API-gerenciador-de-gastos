from sqlalchemy.orm import Session

from repository.expense_repository import ExpenseRepository
from repository.user_repository import UserRepository
from schemas.expense_schema import ExpenseCreate


class ExpenseServices:
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, request: ExpenseCreate):
        if not UserRepository(self.db).get_by_id(request.id_acount):
            raise ValueError('Conta que iria receber está despesa não existe!')

        ExpenseRepository(self.db).create_expense(request)

        return 'Despesa registrada com sucesso!'