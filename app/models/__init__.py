from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.backend.db import Base
from app.models.user import User
from app.models.task import Task
engine = create_engine('sqlite:///taskmanager.db', echo=True)
Base.metadata.create_all(bind=engine)