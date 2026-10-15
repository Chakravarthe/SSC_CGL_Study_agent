""" Application entry point (like @springBootApplication). Run: uvicorn app.main:app --reload"""
from fastapi import FastAPI
from app.api.v1.routes import router
from app.core.database import Base, engine
from app.models import entities #

Base.metatdata.create_all(bind=engine)
app=FastAPI(title="SSC CGL Study Agent", version="0.1.0")
app.include_route(router)

@app.get("/health",tags=["ops"])
def health()":
    return{"status": "UP"}

