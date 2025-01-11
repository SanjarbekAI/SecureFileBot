import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from src.config.env_variables import DATABASE_URL

database = databases.Database(DATABASE_URL)

Base = declarative_base()
metadata = sqlalchemy.MetaData()
