from fastapi import FastAPI
from routes.ingredients import router as ingredients_router
from routes.users import router as users_router
from routes.recipes import router as recipes_router
app = FastAPI()

app.include_router(ingredients_router)
app.include_router(users_router)
app.include_router(recipes_router)