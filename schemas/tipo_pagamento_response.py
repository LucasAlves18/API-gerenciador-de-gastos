from pydantic import BaseModel


class TipoPagamentoResponse(BaseModel):
    id: int
    descricao: str

    class Config:
        from_attributes = True
