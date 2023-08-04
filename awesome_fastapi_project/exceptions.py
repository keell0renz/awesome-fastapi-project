from fastapi import FastAPI
from fastapi.responses import JSONResponse
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError

app = FastAPI()

class MyCustomException(Exception):
    def __init__(self, message: str):
        self.message = message

class UserIsNotAuthenticated(Exception):
    def __init__(self, message: str = None):
        self.message = message

class JWTAuthException(Exception):
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

@app.exception_handler(InvalidTokenError)
async def invalid_token_error_handler(request, exc):
    return JSONResponse(
        status_code=401,
        content={"message": f"Oops! Invalid token! {exc}"}
    )

@app.exception_handler(ExpiredSignatureError)
async def expired_signature_error_handler(request, exc):
    return JSONResponse(
        status_code=401,
        content={"message": f"Oops! Token has expired! {exc}"}
    )

@app.exception_handler(JWTAuthException)
async def jwt_auth_exception_handler(request, exc):
    return JSONResponse(
        status_code=401,
        content={"message": f"Oops! JWT authentication failed! {exc}"}
    )