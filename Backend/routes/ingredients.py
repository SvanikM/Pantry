from fastapi import APIRouter
from db import get_db
from schemas import IngredientCreate

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
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient added successfully"}