from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from fastapi_jwt_auth import AuthJWT

from .authentication import get_current_user
from .authorization import Ensure

router = APIRouter()

@cbv(router)
class UserView:
    @router.get("/")
    def get_users(self):
        return {"message": "Hello World! Are you lost? This is not the page you're looking for."}

    @router.post("/")
    def create_user(self):
        return {"message": "Hello World! You just created a user. Congratulations, you're now a parent!"}

    @router.get("/{user_id}")
    def get_user(self, user_id: int):
        return {"message": f"Hello World! You're looking for user {user_id}? Sorry, they're on vacation in Hawaii."}

    @router.put("/{user_id}")
    def update_user(self, user_id: int):
        return {"message": f"Hello World! User {user_id} has been updated. They now have a new hat."}

    @router.delete("/{user_id}")
    def delete_user(self, user_id: int):
        return {"message": f"Hello World! User {user_id} has been deleted. Don't worry, they'll be back in the sequel."}
    
@cbv(router)
class AuthView:
    @router.post("/login")
    def login(self, credentials: dict, Authorize: AuthJWT = Depends()):
        if credentials["username"] != "testuser" or credentials["password"] != "testpassword":
            return {"error": "Invalid credentials"}
        
        access_token = Authorize.create_access_token(subject=credentials["username"])
        refresh_token = Authorize.create_refresh_token(subject=credentials["username"])

        return {"access_token": access_token, "refresh_token": refresh_token}

    @router.post("/refresh")
    def refresh(self, Authorize: AuthJWT = Depends()):
        Authorize.jwt_refresh_token_required()

        current_user = Authorize.get_jwt_subject()

        access_token = Authorize.create_access_token(subject=current_user.username)

        return {"access_token": access_token}

    @router.get("/protected")
    def protected(self, user = Depends(get_current_user)):
        return {"message": f"Hello World! You're authenticated as {user}."}