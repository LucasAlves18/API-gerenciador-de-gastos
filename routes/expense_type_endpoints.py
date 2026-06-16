from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from authentication.dependencias import get_current_user
from infrastructure.database import get_db
from schemas.expense_type_schema import ExpenseTypeCreate
from fastapi import Request
from authentication.rate_limit import limiter
from services.expense_type_services import ExpenseTypeService

router = APIRouter()

@router.post("/expense-type/add",
            tags=['Expenser'],
            summary='endpoint cria um novo tipo de gasto')
@limiter.limit("5/minute")
def search_user(
        request: Request,
        body: ExpenseTypeCreate,
        db: Session = Depends(get_db),
        _=Depends(get_current_user)):
    try:
        return ExpenseTypeService(db).create_expense_type(body)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail='Erro inesperado!')
