from flask import request, make_response
from flask.json import jsonify
from utils.auth import *
from main import app
from repository import user_details_db


@app.route("/api/auth/register", methods=['POST'])
def register():
    try:
        """
            this api used to register the user at Xpenditure
            request param: username, password, fName, lName, phoneno, addressLine1, street, province, zipCode, country
        """
        data = request.get_json()
        app.logger.info(data)

        userDetailsDb = user_details_db.UserDetailsDB()
        res = userDetailsDb.register(data["username"], data["password"], data["fName"], data["lName"],
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


@app.route("/api/users/profile")
@auth_required
def get_profile():
    try:
        """
            fetches the user profile information for current logged-in user
        """
        userDetailsDb = user_details_db.UserDetailsDB()
        res = userDetailsDb.get_user_details_from_user_id()
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
        app.logger.error("Exception in get_profile: %s", err)
        abort(500)


@app.route("/api/users/profileUpdate", methods=['POST'])
@auth_required
def save_profile():
    try:
        """
            used to update the profile information for current user
            request param: uId, username, password, fName, lName, phoneno, addressLine1, street, province, zipCode, country
        """
        data = request.get_json()
        userDetailsDb = user_details_db.UserDetailsDB()
        res = userDetailsDb.update_user_details(data["uId"], data["fName"], data["lName"], data["phoneno"], data["addressLine1"], data["street"], data["province"], data["zipCode"], data["country"])
        if res is not None:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Profile updated successfully!",
                "data": res
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in get_profile: %s", err)
        abort(500)
