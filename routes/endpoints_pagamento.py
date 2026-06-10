from sqlalchemy.orm import Session
from infraestrutura.database import get_db
from services.services_pagamentos import ServicePagamentos
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

@router.get("/pagamentos/tipos",
            tags=['PAGAMENTOS'],
            summary='endpoint retorna os tipos de pagamentos existentes'
            )
def buscar_tipo_pagamento(_= Depends(oauth2_scheme),
                          db: Session = Depends(get_db)):
    return ServicePagamentos.buscar_tipo_pagamento(db)
