from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth,routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
# from app.core.exceptions import register_exception_handlers
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app= FastAPI(title='Car price predictor API')

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )


#link middleware
app.add_middleware(LoggingMiddleware)

#link endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Prediction'])

#monitoring using Prometheus
Instrumentator().instrument(app).expose(app)

# add exception_handler
# register_exception_handlers(app)