import uvicorn
from fastapi import FastAPI
from routes.user_endpoints import router as router_user
from routes.auth_endpoints import router as router_auth
from infrastructure import database
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from authentication.rate_limit import limiter

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app = FastAPI()

app.include_router(router_user)
app.include_router(router_auth)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9065, reload=True)
    print()