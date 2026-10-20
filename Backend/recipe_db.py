import os
from dotenv import load_dotenv
import pymongo

MONGODB_URI = os.getenv("MONGO_LINK")
'''
Recipes:
-RecipeID
-UserID
-Array of Ingredients(Object in schema.py)

Saved Recipes:
-UserID
-RecipeID
'''