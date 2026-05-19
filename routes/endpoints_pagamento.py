from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infraestrutura.database import get_db
from schemas.tipo_pagamento_response import TipoPagamentoResponse
from services.services_pagamentos import ServicePagamentos
router = APIRouter()

@router.get("/pagamentos/tipos",
            tags=['PAGAMENTOS'],
            summary='endpoint retorna os tipos de pagamentos existentes',
            response_model=list[TipoPagamentoResponse]
            )
def buscar_tipo_pagamento(db: Session = Depends(get_db)):
    return ServicePagamentos.buscar_tipo_pagamento(db)
