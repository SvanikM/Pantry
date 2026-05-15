from fastapi import APIRouter
from db import get_db
from schemas import IngredientCreate
from schemas import IngredientUpdate

router = APIRouter()

@router.post("/ingredients/create")
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
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient added successfully"}

@router.post("/ingredients/update")
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
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient updated successfully"}

