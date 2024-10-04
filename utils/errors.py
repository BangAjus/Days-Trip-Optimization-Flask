from flask_smorest import Blueprint
from flask import jsonify

errorsBp = Blueprint("errors", __name__)

@errorsBp.app_errorhandler(400)
def bad_request(error):
    return jsonify({
        "status": {
            "code": 400,
            "message": "Client side error!"
        },
        "data": None,
    }), 400


@errorsBp.app_errorhandler(404)
def not_found(error):
    return jsonify({
        "status": {
            "code": 404,
            "message": "URL not found!"
        },
        "data": None,
    }), 404


@errorsBp.app_errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "status": {
            "code": 405,
            "message": "Request method not allowed!"
        },
        "data": None,
    }), 405


@errorsBp.app_errorhandler(429)
def rate_limit_exceeded(error):
    return jsonify({
        "status": {
            "code": 429,
            "message": "Rate limit exceeded. Please try again later."
        },
        "data": None
    }), 429


@errorsBp.app_errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "status": {
            "code": 500,
            "message": "Server error!"
        },
        "data": None,
    }), 500