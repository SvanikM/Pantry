from fastapi import APIRouter
from db import get_db
from schemas import UserCreate


router = APIRouter()

@router.post("/users")
def add_user(user: UserCreate):
    mydb = get_db()
    cursor = mydb.cursor()

    query = """
    INSERT INTO users (UserName, Email, Password)
    VALUES (%s, %s, %s)
    """

    values = (
        user.username,
        user.email,
        user.password,
    )

    cursor.execute(query, values)
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "Ingredient added successfully"}