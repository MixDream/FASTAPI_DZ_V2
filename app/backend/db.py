#.\.venv\Scripts\activate активация окружения
#uvicorn dz:app --reload
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine= create_engine("sqlite:///taskmanager.db", echo= True)

SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass