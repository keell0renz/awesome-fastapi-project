from .exceptions import app

from .user.routers import router as user_router
from .posts.routers import router as posts_router

from .config import config
from .logging import logger

from tortoise.contrib.fastapi import register_tortoise

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(posts_router, prefix="/posts", tags=["posts"])

logger.debug(f"Production Databse URL: {config.production_database_url}")
logger.debug(f"Test Database URL: {config.test_database_url}")
logger.debug(f"Database URL: {config.database_url}")

TORTOISE_ORM = {
    "connections": {"default": config.database_url},
    "apps": {
        "models": {
            "models": ["awesome_fastapi_project.user.models", "awesome_fastapi_project.posts.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)