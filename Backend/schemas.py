from pydantic import BaseModel

class IngredientObject(BaseModel):
    item: str
    quantity: int
    unit: str | None = None

class UserObject(BaseModel):
    username: str
    email: str
    password: str
