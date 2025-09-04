from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.product import router_product
from app.database.database import Base, engine

app = FastAPI()

app.include_router(router_product)

allow_origins = [
    "http://localhost",   # frontend en Docker
    "http://localhost:5173",  # desarrollo local (vite)
    "https://midominio.com",  # producción
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

Base.metadata.create_all(bind=engine)