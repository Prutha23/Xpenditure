from flask import request, make_response
from flask.json import jsonify
from utils.auth import *
from main import app
from repository import subscription_db
from datetime import date
from dateutil.relativedelta import relativedelta


@app.route("/api/subscription/payment", methods=['POST'])
@auth_required
def payment():
    try:
        """
            this api uses to receive the payment for user so once admin approve the payment user will be converted to premium user
            Note: we have not integrated any payment gateway
            request param: PAYMENT_METHOD, CARD_HOLDER_NAME, CARD_NO
        """
        data = request.get_json()
        db = subscription_db.SubscriptionDB()
        date_after_month = date.today() + relativedelta(months=1)

        res = db.receive_payment(data["PAYMENT_METHOD"], data["CARD_HOLDER_NAME"], data["CARD_NO"], date_after_month.strftime('%Y-%m-%d'))
        if res is not None:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Payment received successfully, please wait for admin to approve the request.",
                "data": res
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in get_dashboard_data: %s", err)
        abort(500)


@app.route("/api/subscription/approve", methods=['POST'])
@admin_required
def approve_payment():
    try:
        """
            this api is used to update the user status to premium when admin clicks on approve button
            request param: user_id, start_date, end_date
        """
        data = request.get_json()
        db = subscription_db.SubscriptionDB()

        res = db.approve_payment(data["user_id"], data["start_date"], data["end_date"])
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
        app.logger.error("Exception in approve_payment: %s", err)
        abort(500)
