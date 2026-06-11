from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from schemas.user_schema import UserLogin
from services.auth_service import Auth
router = APIRouter()

@router.post("/login",
            tags=['Auth'],
            summary='Realiza login do user'
            )
def login(request: UserLogin,
          db: Session = Depends(get_db)):

    try:
        return Auth.login(db, request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail='Erro inesperado!')
