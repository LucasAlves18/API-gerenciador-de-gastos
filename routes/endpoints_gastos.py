from fastapi import APIRouter
router = APIRouter()

@router.get("/gastos",
            tags=['GASTOS'],
            summary='endpoint retorna os gastos do usuário logado'
            )
def listar_gastos():
    return 'teste'