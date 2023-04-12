from flask import request, make_response
from flask.json import jsonify
from utils.auth import *
from main import app
from repository import user_db


@app.route("/api/auth/register", methods=['POST'])
def register():
    try:
        data = request.get_json()
        app.logger.info(data)

        userDb = user_db.UserDB()
        res = userDb.add_user_and_user_details(data["username"], data["password"], data["fName"], data["lName"],
                                               data["phoneno"], data["addressLine1"], data["street"],
                                               data["province"], data["zipCode"], data["country"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in register: %s", err)
        abort(500)


@app.route("/api/users/getAll")
@admin_required
def get_all():
    try:
        obj = user_db.UserDB()
        res = obj.get_all()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in get_all: %s", err)
        abort(500)


@app.route("/api/users/updateActiveStatus", methods=['POST'])
@admin_required
def update_active_status():
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
        app.logger.error("Exception in update_active_status: %s", err)
        abort(500)


@app.route("/api/admin/count")
@admin_required
def get_admin_counts():
    try:
        obj = user_db.UserDB()
        res = obj.get_admin_counts()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in get_admin_counts: %s", err)
        abort(500)