from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from .authentication import get_current_user


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