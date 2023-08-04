from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

class MyCustomException(Exception):
    def __init__(self, message: str):
        self.message = message

class UserIsNotAuthenticated(Exception):
    def __init__(self, message: str = None):
        self.message = message

@app.exception_handler(MyCustomException)
async def unicorn_exception_handler(request, exc):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.message} did something. There goes a rainbow... I am a teapot, bitch."},
    )

@app.exception_handler(UserIsNotAuthenticated)
async def user_is_not_authenticated_exception_handler(request, exc):
    return JSONResponse(
        status_code=403,
        content={"message": f"Oops! You are not authenticated! {exc.message}"}
    )