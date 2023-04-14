from flask import request, make_response
from flask.json import jsonify
from utils.auth import *
from main import app
from repository import user_db


@app.route("/api/user/dashboard")
@auth_required
def get_dashboard_data():
    try:
        userDb = user_db.UserDB()
        res = userDb.get_user_dashboard_data()
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
        app.logger.error("Exception in get_dashboard_data: %s", err)
        abort(500)
