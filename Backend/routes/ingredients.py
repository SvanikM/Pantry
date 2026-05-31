from fastapi import APIRouter
from db import get_db
from schemas import IngredientCreate
from schemas import IngredientUpdate

router = APIRouter()

@router.post("/ingredients")
def add_ingredient(ingredient: IngredientCreate):
    mydb = get_db()
    cursor = mydb.cursor()

    query = """
    INSERT INTO ingredients (UserName, Email, IngredientName, IngredientQuantity, IngredientUnit)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        ingredient.username,
        ingredient.email,
        ingredient.item,
        ingredient.quantity,
        ingredient.unit
    )

    cursor.execute(query, values)
    if cursor.rowcount == 0:
        return {"message": "Failed to add ingredient"}
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient added successfully"}

@router.patch("/ingredients")
def update_ingredient(ingredient: IngredientUpdate):
    mydb = get_db()
    cursor = mydb.cursor()

    query = """
    UPDATE ingredients
    SET IngredientQuantity = %s
    WHERE UserName = %s
    AND Email = %s
    AND IngredientName = %s;
    """

    values = (
        ingredient.quantity,
        ingredient.username,
        ingredient.email,
        ingredient.item
    )

    cursor.execute(query, values)
    if cursor.rowcount == 0:
        return {"message": "Ingredient not found"}
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient updated successfully"}

@router.get("/ingredients")
def get_ingredients(email: str, username: str, item: str):
    mydb = get_db()
    cursor = mydb.cursor()
    query = """
    SELECT IngredientName, IngredientQuantity, IngredientUnit
    FROM ingredients
    WHERE UserName = %s AND Email = %s and IngredientName = %s
    """
    values = (username, email, item)
    cursor.execute(query, values)
    if cursor.rowcount == 0:
        return {"message": "Ingredient not found"}
    ingredients = cursor.fetchall()
    cursor.close()
    mydb.close()
    return ingredients

@router.delete("/ingredients")
def delete_ingredients(email: str, username: str, item: str):
    mydb = get_db()
    cursor = mydb.cursor()
    query = """
    DELETE FROM ingredients
    WHERE UserName = %s AND Email = %s AND IngredientName = %s
    """
    values = (username, email, item)
    cursor.execute(query, values)
    if cursor.rowcount == 0:
        return {"message": "Ingredient not found"}
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Ingredient deleted successfully"}
            
    
