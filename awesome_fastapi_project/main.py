from .exceptions import app

from .user.routers import router as user_router
from .posts.routers import router as posts_router

from .config import config
from .logging import logger

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(posts_router, prefix="/posts", tags=["posts"])

logger.debug(f"Databse URL: {config.database_url}")