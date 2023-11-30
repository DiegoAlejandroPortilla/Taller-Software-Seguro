from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routes.APIOwner import APIOwner

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    return response

app.include_router(APIOwner)
