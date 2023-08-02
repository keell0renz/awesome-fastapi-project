from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

class MyCustomException(Exception):
    def __init__(self, message: str):
        self.message = message

@app.exception_handler(MyCustomException)
async def unicorn_exception_handler(request, exc):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.message} did something. There goes a rainbow... I am a teapot, bitch."},
    )
