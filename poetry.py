import sys
import os

def run_dev(): # Run development server
    os.system(
        "uvicorn awesome_fastapi_project.main:app"
    )

def run_pytest(): # Run pytest
    os.system(
        "pytest"
    )

def run_migrate(): # Run migrations
    os.system(
        "aerich migrate && aerich upgrade"
    )

def run_init_db(): # Initialize database
    os.system(
        "aerich init-db"
    )