import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import APIRouter
from schemas import IngredientObject
from typing import List
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

router = APIRouter()

db = client["PantryDB"]
recipes = db["recipes"]
fav_recipes = db["fav_recipes"]


@router.post("/recipes")
def add_recipe(Ingredients: List[IngredientObject], RecipeName: str, UserName: str, Email: str):
    recipe = {"RecipeName": RecipeName, "UserName": UserName, "Email": Email, 
              "Ingredients": [item.model_dump() for item in Ingredients]}
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