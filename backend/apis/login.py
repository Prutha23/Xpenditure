from flask import request, make_response
from flask.json import jsonify
from utils.auth import *
from main import app


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
        return make_response(jsonify({
            'username': user['username'],
            'is_active': user['is_active'],
            'role': user['role']
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


@app.route('/api/user-sample', methods=['GET', 'POST'])
@auth_required
def sample_api():
    """
    Example API
    """
    if request.method == 'GET':
        return make_response(jsonify({'example': 123}))
    elif request.method == 'POST':
        data = request.get_json()
        app.logger.debug('payload: %d', data['example'])
        return make_response(jsonify({'example': data['example'] * 2}))
    else:
        abort(405)


@app.route('/api/admin-sample', methods=['GET', 'POST'])
@admin_required
def admin_api():
    """
    Example API
    """
    if request.method == 'GET':
        return make_response(jsonify({'example': 123}))
    elif request.method == 'POST':
        data = request.get_json()
        app.logger.debug('payload: %d', data['example'])
        return make_response(jsonify({'example': data['example'] * 2}))
    else:
        abort(405)
