import os
from dotenv import load_dotenv
import pymongo
from fastapi import APIRouter
from schemas import IngredientObject

MONGODB_URI = os.getenv("MONGODB_URI")
router = APIRouter()

db = client["PantryDB"]
recipes = db["recipes"]
fav_recipes = db["fav_recipes"]


@router.post("/recipes")
def add_recipe(Ingredients: List[IngredientObject], RecipeName: str, UserName: str, Email: str):
    recipe = {"RecipeName": RecipeName, "UserName": UserName, "Email": Email, "Ingredients": Ingredients}
    result = recipes.insert_one(recipe)

@router.delete("/recipes")
def remove_recipe(RecipeName: str, UserName: str, Email: str):
    filter = {"RecipeName": RecipeName, "UserName": UserName, "Email": Email}
    result = recipes.delete_one(filter)

@router.get("/recipes")
def get_recipe(RecipeName: str, UserName: str, Email: str):
    filter = {"RecipeName": RecipeName, "UserName": UserName, "Email": Email}
    result = recipes.find_one(filter)

'''
Recipes:
-RecipeName
-UserID
-Array of Ingredients(Object in schema.py)

Saved Recipes:
-UserID
-RecipeName
'''