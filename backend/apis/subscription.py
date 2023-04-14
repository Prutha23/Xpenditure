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
