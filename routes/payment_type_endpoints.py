from typing import Optional
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from authentication.dependencias import get_current_user
from infrastructure.database import get_db
from fastapi import Request
from authentication.rate_limit import limiter
from schemas.payment_type_schema import CreatePaymentType
from services.payment_type_services import PaymentTypeServices

router = APIRouter()

@router.get("/payment-type/search",
            tags=['Payment'],
            summary='endpoint')
@limiter.limit("5/minute")
def search_payment_type(
        request: Request,
        id: Optional[int] = None,
        db: Session = Depends(get_db),
        _=Depends(get_current_user)):
    try:
        return PaymentTypeServices(db).search_payment_type(id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail='Erro inesperado!')


@router.post("/payment-type/create",
            tags=['Payment'],
            summary='endpoint')
@limiter.limit("5/minute")
def search_payment_type(
        request: Request,
        body:CreatePaymentType,
        db: Session = Depends(get_db),
        _=Depends(get_current_user)):
    try:
        return PaymentTypeServices(db).create_payment_type(body)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro inesperado! {e}')