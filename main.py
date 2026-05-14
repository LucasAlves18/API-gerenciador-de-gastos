import uvicorn
from fastapi import FastAPI
from routes.endpoints_gastos import router as router_pagamentos
from infraestrutura import database
app = FastAPI()
app.include_router(router_pagamentos)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9065, reload=True)
    print()