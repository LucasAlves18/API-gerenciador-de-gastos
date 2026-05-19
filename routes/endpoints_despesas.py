from fastapi import APIRouter
router = APIRouter()

@router.get("/despesas/{id_user}",
            tags=['DESPESAS'],
            summary='endpoint retorna os gastos do usuário logado'
            )
def listar_gastos():
    services =  ''