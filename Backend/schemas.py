from pydantic import BaseModel

class IngredientCreate(BaseModel):
    username:str
    email:str
    item: str
    quantity: int
    unit: str | None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str