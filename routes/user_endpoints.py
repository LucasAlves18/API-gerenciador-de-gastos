from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from authentication.dependencias import get_current_user
from infrastructure.database import get_db
from schemas.user_schema import UserCreate
from services.user_services import UserServices
from fastapi import Request
from authentication.rate_limit import limiter

router = APIRouter()

@router.post("/users/create",
            tags=['User'],
            summary='endpoint de criação de usuário'
            )
@limiter.limit("5/minute")
def create_user(
        request: Request,
        body: UserCreate,
        db: Session = Depends(get_db)):
    try:
        return UserServices(db).create_user(body)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail='Erro inesperado')

@router.get("/users/{email}",
            tags=['User'],
            summary='endpoint retorna usuário apartir do email')
@limiter.limit("5/minute")
def search_user(
        request: Request,
        email: str,
        db: Session = Depends(get_db),
        _=Depends(get_current_user)):
    try:
        return UserServices(db).search_user(email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail='Erro inesperado!')
