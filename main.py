import uvicorn
from fastapi import FastAPI
from routes.endpoints_despesas import router as router_despesas
from routes.endpoints_pagamento import router as router_pagamentos
from routes.endpoints_user import router as router_user
from routes.auth import router as router_auth
from infraestrutura import database


app = FastAPI()

app.include_router(router_user)
app.include_router(router_despesas)
app.include_router(router_pagamentos)
app.include_router(router_auth)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9065, reload=True)
    print()