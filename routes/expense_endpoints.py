from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from authentication.dependencias import get_current_user
from infrastructure.database import get_db
from schemas.expense_schema import ExpenseCreate
from services.expense_services import ExpenseServices
from fastapi import Request
from authentication.rate_limit import limiter

router = APIRouter()

@router.get("/expense/add",
            tags=['Expenser'],
            summary='endpoint cria um novo gasto, vinculado a um user e um tipo de pagamento')
@limiter.limit("5/minute")
def search_user(
        request: Request,
        body: ExpenseCreate,
        db: Session = Depends(get_db),
        _=Depends(get_current_user)):
    try:
        return ExpenseServices(db).create_expense(body)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail='Erro inesperado!')
