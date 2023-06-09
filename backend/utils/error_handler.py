from werkzeug.exceptions import HTTPException
from flask.json import jsonify
from main import app


def error_handler(error):
    """
    Standard Error Handler
    """
    if isinstance(error, HTTPException):
        return jsonify({
            'statusCode': error.code,
            'status': 'Error',
            'message': error.name,
            'description': error.description
        }), error.code
    else:
        return jsonify({
            'statusCode': 500,
            'status': 'Error',
            'message': 'Internal Server Error',
            'description': 'An unknown error has occurred'
        }), 500


# common errors - add others as needed
app.register_error_handler(400, error_handler)
app.register_error_handler(401, error_handler)
app.register_error_handler(403, error_handler)
app.register_error_handler(404, error_handler)
app.register_error_handler(405, error_handler)
app.register_error_handler(500, error_handler)
