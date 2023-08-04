from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import MissingTokenError
from pydantic import BaseModel

@AuthJWT.load_config
def get_config():
    """
        AuthJWT configuration.
    """
    class Settings(BaseModel):
        authjwt_secret_key: str = "330081334a2c3623d599350c3912dbed72e3a5b2edc13457d6268de733badb57"

    return Settings()

async def get_current_user(Authorize: AuthJWT = Depends()):
    """
        Get current user.
    """

    Authorize.jwt_required()

    user = Authorize.get_jwt_subject()

    return "anonymous" if user is None else user