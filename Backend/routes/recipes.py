import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError
from fastapi import APIRouter
from schemas import IngredientObject
from typing import List
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

router = APIRouter()

db = client["PantryDB"]
recipes = db["recipes"]
#UserName+Email+RecipeName is the primary key
recipes.create_index(
    [
        ("UserName", 1),
        ("Email", 1),
        ("RecipeName", 1)
    ],
    unique=True,
    name="RecipeID"
)
fav_recipes = db["fav_recipes"]
'''
fav_recipes.create_index(
    [
        ("UserName", 1),
        ("Email", 1),
    ]
)
'''

@router.post("/recipes")
def add_recipe(Ingredients: List[IngredientObject], RecipeName: str, UserName: str, Email: str):
    recipe = {"RecipeName": RecipeName, "UserName": UserName, "Email": Email, 
              "Ingredients": [item.model_dump() for item in Ingredients]}
    try:
        result = recipes.insert_one(recipe)
        return{
            "message": "Recipe added succesfully",
            "id": str(result.inserted_id)
            }
    except DuplicateKeyError:
        return{
            "message": "Insert failed, a recipe with this name already exists on this account"
            }
    except PyMongoError as err:
        return{
            "message": "MongoDB error",
            "error": str(err) #typecasting error to a string so it fits in the json format
            }
    

@router.delete("/recipes")
def remove_recipe(RecipeName: str, UserName: str, Email: str):
    filter = {"RecipeName": RecipeName, "UserName": UserName, "Email": Email}
    try:
        result = recipes.delete_one(filter)
        if(result.deleted_count == 1):
            return {"message": "Deleted Successfully"}
        elif(result.deleted_count == 0):
            return {"message": "Deletion failed"}
        else:
            return {"message": "Undefined, not sure what happened"}
    except PyMongoError as err:
        return{
            "message": "MongoDB error",
            "error": str(err)
        }


@router.get("/recipes")
def get_recipe(RecipeName: str, UserName: str, Email: str):
    filter = {"RecipeName": RecipeName, "UserName": UserName, "Email": Email}
    result = recipes.find_one(filter)

    if result is None:
        return {"message": "Recipe not found"}
    
    #converting id so it can return as JSON
    result["_id"] = str(result["_id"])
    return result

'''
Recipes:
-RecipeName
-UserID
-Array of Ingredients(Object in schema.py)

Saved Recipes:
-UserID
-RecipeName
'''