from flask import request, make_response
from flask.json import jsonify
from utils.auth import *
from main import app
from repository import user_db


@app.route('/api/auth/login', methods=['POST'])
def login_api():
    """
    Login user
    """
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        access_token, refresh_token = authenticate_user(username, password)
        return make_response(jsonify({
            'accessToken': access_token,
            'refreshToken': refresh_token
        }))
    except AuthenticationError as error:
        app.logger.error('authentication error: %s', error)
        abort(403)


@app.route('/api/auth/info', methods=['GET'])
@auth_required
def login_info_api():
    """
    Get informaiton about currently logged in user
    """
    try:
        user = get_authenticated_user()
        userDb = user_db.UserDB()
        return make_response(jsonify({
            'username': user['username'],
            'is_active': user['is_active'],
            'role': user['role'],
            'is_premium': userDb.get_is_premium(user['username'])
        }))
    except AuthenticationError as error:
        app.logger.error('authentication error: %s', error)
        abort(403)


@app.route('/api/auth/logout', methods=['POST'])
@auth_refresh_required
def logout_api2():
    """
    Log user out
    """
    deauthenticate_user()
    return make_response()


@app.route('/api/auth/refresh', methods=['POST'])
@auth_refresh_required
def refresh_api():
    """
    Get a fresh access token from a valid refresh token
    """
    try:
        access_token = refresh_authentication()
        return make_response(jsonify({
            'accessToken': access_token
        }))
    except AuthenticationError as error:
        app.logger.error('authentication error %s', error)
        abort(403)
