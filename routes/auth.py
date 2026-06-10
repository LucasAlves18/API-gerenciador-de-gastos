from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from infraestrutura.database import get_db
from schemas.user import UserLogin
from services.auth import Auth
router = APIRouter()

@router.post("/login",
            tags=['Auth'],
            summary='Realiza login do user'
            )
def login(request: UserLogin,
          db: Session = Depends(get_db)):

    response = Auth.login(db, request)
    return response
