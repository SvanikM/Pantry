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
    if cursor.rowcount == 0:
        return {"message": "Failed to add ingredient"}
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient added successfully"}

@router.patch("/ingredients")
def update_ingredient(username: str, email: str, item: str, quantity: int | None = None, unit: str | None = None):
    mydb = get_db()
    cursor = mydb.cursor()

    if quantity is None and unit is None:
        return {"message": "No fields to update"}
    #update quantity
    elif quantity is not None and unit is None:
        query = """
        UPDATE ingredients
        SET IngredientQuantity = %s
        WHERE UserName = %s
        AND Email = %s
        AND IngredientName = %s;
        """

        values = (
            quantity,
            username,
            email,
            item
        )
    #update unit
    elif quantity is None and unit is not None:
        query = """
        UPDATE ingredients
        SET IngredientUnit = %s
        WHERE UserName = %s
        AND Email = %s
        AND IngredientName = %s;
        """

        values = (
            unit,
            username,
            email,
            item
        )

    #update quantity & unit
    else:
        query = """
        UPDATE ingredients
        SET IngredientQuantity = %s, IngredientUnit = %s
        WHERE UserName = %s
        AND Email = %s
        AND IngredientName = %s;
        """

        values = (
            quantity,
            unit,
            username,
            email,
            item
        )

    cursor.execute(query, values)
    if cursor.rowcount == 0:
        return {"message": "Ingredient not found"}
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient updated successfully"}

#accepts the following sort types: AlphabeticalAsc, AlphabeticalDesc, QuantityAsc, QuantityDesc
@router.get("/ingredients")
def get_ingredients(email: str, username: str, item: str, sort: str):
    mydb = get_db()
    cursor = mydb.cursor()
    query = """
    SELECT IngredientName, IngredientQuantity, IngredientUnit
    FROM ingredients
    WHERE UserName = %s AND Email = %s and IngredientName LIKE CONCAT('%', %s, '%')
    """
    if sort == "AlphabeticalAsc":
        query += " ORDER BY IngredientName ASC"
    elif sort == "AlphabeticalDesc":
        query += " ORDER BY IngredientName DESC"
    elif sort == "QuantityAsc":
        query += " ORDER BY IngredientQuantity ASC"
    elif sort == "QuantityDesc":
        query += " ORDER BY IngredientQuantity DESC"

    values = (username, email, item)
    cursor.execute(query, values)
    ingredients = cursor.fetchall()
    if cursor.rowcount == 0:
        return {"message": "Ingredient not found"}
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
            
    
