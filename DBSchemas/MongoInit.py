import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

db = client["PantryDB"]
recipes = db["recipes"]
fav_recipes = db["fav_recipes"]

recipes.insert_one({"empty1": "empty1"})

fav_recipes.insert_one({"empty": "empty"})

'''
Recipes:
-RecipeID
-UserID
-Array of Ingredients(Object in schema.py)

Saved Recipes:
-UserID
-RecipeID
'''

