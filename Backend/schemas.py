from pydantic import BaseModel

class Ingredient(BaseModel):
    item: str
    quantity: int
    unit: str | None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
