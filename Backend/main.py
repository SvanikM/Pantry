from fastapi import FastAPI
from routes.ingredients import router as ingredients_router

app = FastAPI()

app.include_router(ingredients_router)