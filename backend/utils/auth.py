from functools import wraps
from flask import abort
from flask_jwt_extended import (create_access_token, create_refresh_token, get_jwt_identity, verify_jwt_in_request)
from main import app
from repository.user_db import UserDB


class AuthenticationError(Exception):
    """Base Authentication Exception"""
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return self.__class__.__name__ + '(' + str(self.msg) + ')'


class InvalidCredentials(AuthenticationError):
    """Invalid username/password"""


class AccountInactive(AuthenticationError):
    """Account is disabled"""


class AccessDenied(AuthenticationError):
    """Access is denied"""


class UserNotFound(AuthenticationError):
    """User identity not found"""


def authenticate_user(username, password):
    """
    Authenticate a user
    """
    user_db_obj = UserDB()
    user_dit = user_db_obj.get_user_from_username(username)
    if user_dit["is_active"] == 1:
        if user_dit["password"] == password:
            return (
                create_access_token(identity=username),
                create_refresh_token(identity=username)
            )
        else:
            raise InvalidCredentials()
    else:
        raise AccountInactive(username)


def get_authenticated_user():
    """
    Get authentication token user identity and verify account is active
    """
    identity = get_jwt_identity()
    user_db_obj = UserDB()
    user_dit = user_db_obj.get_user_from_username(identity)
    if user_dit:
        if user_dit['is_active'] == 1:
            return user_dit
        else:
            raise AccountInactive()
    else:
        raise UserNotFound(identity)


def deauthenticate_user():
    """
    Log user out - need to implement
    """
    identity = get_jwt_identity()
    app.logger.debug('logging user "%s" out', identity)


def refresh_authentication():
    """
    Refresh authentication, issue new access token
    """
    user = get_authenticated_user()
    return create_access_token(identity=user['username'])


def auth_required(func):
    """
    View decorator - require valid access token
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        try:
            get_authenticated_user()
            return func(*args, **kwargs)
        except (UserNotFound, AccountInactive) as error:
            app.logger.error('authorization failed: %s', error)
            abort(403)
    return wrapper


def auth_refresh_required(func):
    """
    View decorator - require valid refresh token
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        try:
            get_authenticated_user()
            return func(*args, **kwargs)
        except (UserNotFound, AccountInactive) as error:
            app.logger.error('authorization failed: %s', error)
            abort(403)
    return wrapper


def admin_required(func):
    """
    View decorator - required valid access token and admin access
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        try:
            user = get_authenticated_user()
            # role = 2 is for admin and role = 1 is for user
            if user['role'] == 2:
                return func(*args, **kwargs)
            else:
                abort(403)
        except (UserNotFound, AccountInactive) as error:
            app.logger.error('authorization failed: %s', error)
            abort(403)
    return wrapper


def get_current_user():
    verify_jwt_in_request()
    user = get_authenticated_user()
    return user


def get_current_user_id():
    verify_jwt_in_request()
    user = get_authenticated_user()
    return user["ID"]


def check_is_premium():
    verify_jwt_in_request()
    username = get_jwt_identity()
    obj = UserDB()
    return obj.get_is_premium(username)
