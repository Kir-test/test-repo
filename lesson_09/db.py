import os

from sqlalchemy import create_engine


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Переменная DATABASE_URL не задана")

engine = create_engine(DATABASE_URL)
