from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "username" VARCHAR(100) NOT NULL UNIQUE,
    "password" VARCHAR(100) NOT NULL,
    "is_active" INT NOT NULL  DEFAULT 1,
    "is_superuser" INT NOT NULL  DEFAULT 0,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "users";"""
