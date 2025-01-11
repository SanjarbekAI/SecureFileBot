# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.env_variables import DATABASE_URL

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Define the Base class for models
Base = declarative_base()

# Async session factory
async_session_maker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
