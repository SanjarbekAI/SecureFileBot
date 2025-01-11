import sqlalchemy
from sqlalchemy import DateTime, func

from src.config.constants import UserStatus
from src.config.database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50), nullable=True),
    sqlalchemy.Column("full_name", sqlalchemy.String(100), nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String(10)),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger, unique=True),
    sqlalchemy.Column("phone_number", sqlalchemy.String(20), nullable=True),
    sqlalchemy.Column(
        "status",
        sqlalchemy.String(20),
        server_default=sqlalchemy.text(f"'{UserStatus.active}'"),
    ),
    sqlalchemy.Column(
        "created_at", DateTime(timezone=True), server_default=func.now()
    ),
    sqlalchemy.Column(
        "updated_at", DateTime(timezone=True), onupdate=func.now()
    ),
)
