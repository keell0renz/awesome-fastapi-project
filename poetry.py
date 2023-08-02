import os

def run_dev(): # Run development server
    os.system(
        "uvicorn awesome_fastapi_project.main:app"
    )