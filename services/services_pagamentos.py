from fastapi import HTTPException
from sqlalchemy.orm import Session
from infraestrutura.models.tipo_pagamento_map import TipoPagamento
from entitys.entity_tipo_pagamento import EntityPagamento


class ServicePagamentos:
    @staticmethod
    def buscar_tipo_pagamento(db: Session):
        try:
            consulta = TipoPagamento.buscar_tipo_pagamento(db)

            if not consulta:
                raise HTTPException(status_code=404, detail="Nenhum tipo de pagamento encontrado!")

            return [EntityPagamento(dados.id, dados.descricao) for dados in consulta]

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail='Erro inesperado, contate o suporte!')
