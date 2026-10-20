import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

db = client["PantryDB"]
recipes = db["recipes"]
saved_recipes = db["saved_recipes"]
