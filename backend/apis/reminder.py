from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import reminder_db
from utils.auth import auth_required, abort


@app.route("/api/reminder/getAllForCurrentUser")
@auth_required
def get_all_reminders_for_current_user():
    try:
        obj = reminder_db.ReminderDB()
        res = obj.getall_for_current_user()
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
        app.logger.error("Exception in getAllForCurrentUser: %s", err)
        abort(500)


@app.route("/api/reminder/addReminder", methods=['POST'])
@auth_required
def add_reminder():
    try:
        # email, due_date, description
        data = request.get_json()
        obj = reminder_db.ReminderDB()
        res = obj.add_reminder(data["EMAIL"], data["DUE_DATE"], data["DESCRIPTION"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Reminder has been added successfully!"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in reminder add: %s", err)
        abort(500)


@app.route("/api/reminder/editReminder", methods=['POST'])
@auth_required
def update_reminder():
    try:
        # id, email, due_date, description
        data = request.get_json()
        obj = reminder_db.ReminderDB()
        res = obj.update_reminder(data["ID"], data["EMAIL"], data["DUE_DATE"], data["DESCRIPTION"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Reminder has been updated successfully!"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in reminder update: %s", err)
        abort(500)


@app.route("/api/reminder/deleteReminder", methods=['POST'])
@auth_required
def delete_reminder():
    try:
        # id
        data = request.get_json()
        obj = reminder_db.ReminderDB()
        res = obj.delete_reminder(data["ID"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Reminder has been deleted successfully!"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in reminder delete: %s", err)
        abort(500)
