import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = "hrone_db"


print("MONGO_URL:", MONGO_URL)

