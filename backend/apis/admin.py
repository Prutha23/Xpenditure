from flask import request, make_response
from flask.json import jsonify
from utils.auth import *
from main import app
from repository import user_db


@app.route("/api/admin/getAllUsers")
@admin_required
def get_all_users():
    try:
        obj = user_db.UserDB()
        res = obj.get_all()
        if res is not None:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in get_all_users: %s", err)
        abort(500)


@app.route("/api/admin/updateUserActiveStatus", methods=['POST'])
@admin_required
def update_user_active_status():
    try:
        data = request.get_json()
        obj = user_db.UserDB()
        res = obj.update_active_status(data["ID"], data["IS_ACTIVE"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in updateUserActiveStatus: %s", err)
        abort(500)


@app.route("/api/admin/count")
@admin_required
def get_admin_dashboard_counts():
    try:
        obj = user_db.UserDB()
        res = obj.get_admin_dashboard_data()
        if res is not None:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in get_admin_dashboard_counts: %s", err)
        abort(500)
