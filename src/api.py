from fastapi import FastAPI

from src.config import fastApiConfig
from src.db import MongoEngine
from src.routes import log_routes

app = FastAPI(**fastApiConfig)
db = MongoEngine().get_connection()

app.include_router(log_routes)
