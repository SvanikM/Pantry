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
    if cursor.rowcount == 0:
        return {"message": "Failed to add user"}
    mydb.commit()

    cursor.close()
    mydb.close()

    return {"message": "User added successfully"}

@router.get("/users")
def get_user(username: str, email: str, password: str | None = None):
    mydb = get_db()
    cursor = mydb.cursor()

    if password is not None:
        query = """
        SELECT UserName, Email, Password
        FROM users
        WHERE UserName = %s AND Email = %s AND Password = %s
        """
        values = (username, email, password)
    
    elif password is None:
        query = """
        SELECT UserName, Email 
        FROM users
        WHERE UserName = %s AND Email = %s
    """
        values = (username, email)
    cursor.execute(query, values)
    user = cursor.fetchone()
    if cursor.rowcount == 0:
        return {"message": "User not found"}
    cursor.close()
    mydb.close()
    return {"users": user}

@router.delete("/users")
def delete_user(username: str, email: str):
    mydb = get_db()
    cursor = mydb.cursor()
    query = """
    DELETE FROM users
    WHERE UserName = %s AND Email = %s
    """
    values = (username, email)
    cursor.execute(query, values)
    if cursor.rowcount == 0:
        return {"message": "User not found"}
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "User deleted successfully"}
