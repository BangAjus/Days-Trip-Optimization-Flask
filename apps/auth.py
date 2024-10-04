import os
from flask_httpauth import HTTPTokenAuth
from dotenv import load_dotenv

load_dotenv()

auth = HTTPTokenAuth(scheme='Bearer')
valid_token = os.getenv("SECRET_KEY")

@auth.verify_token
def verify_token(token):
    if token == valid_token:
        return "Valid User"
    return None

@auth.error_handler
def unauthorized():
    return {
        "status": {
            "code": 401,
            "message": "Unauthorized Access!"
        },
        "data": None,
    }, 401 