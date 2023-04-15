from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import expense_db
from utils.auth import auth_required, abort


@app.route("/api/expense/getAllForCurrentUser")
@auth_required
def get_all_for_current_user():
    try:
        """
            this api returns all expenses created by them to show on expense page 
        """
        obj = expense_db.ExpenseDB()
        res = obj.getall_expenses_for_current_user()
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


@app.route("/api/expense/getByCategoryId")
@auth_required
def get_by_category_id():
    try:
        """
            it will return the expense for particular category
            request param: cat_id
        """
        args = request.args.to_dict()
        obj = expense_db.ExpenseDB()
        res = obj.get_expense_from_category_id(args["cat_id"])
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
        app.logger.error("Exception in getByCategoryId: %s", err)
        abort(500)


@app.route("/api/expense/addExpense", methods=['POST'])
@auth_required
def add_expense():
    try:
        """
            this api used to add new expense in Expense table
            request param:  cat_id, amount, description, expense_date
        """
        data = request.get_json()
        obj = expense_db.ExpenseDB()
        res = obj.add_expense(data["cat_id"], data["amount"], data["description"], data["expense_date"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Expense has been added successfully!"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in expense add: %s", err)
        abort(500)


@app.route("/api/expense/editExpense", methods=['POST'])
@auth_required
def update_expense():
    try:
        """
            this api used to update the information of already created expense
            request param: ID, cat_id, amount, description, expense_date
        """
        data = request.get_json()
        obj = expense_db.ExpenseDB()
        res = obj.update_expense(data["ID"], data["cat_id"], data["amount"], data["description"], data["expense_date"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Expense has been updated successfully!"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in expense update: %s", err)
        abort(500)


@app.route("/api/expense/deleteExpense", methods=['POST'])
@auth_required
def delete_expense():
    try:
        """
            this api used to delete the expense
            request param: id
        """
        data = request.get_json()
        obj = expense_db.ExpenseDB()
        res = obj.delete_expense(data["id"])
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Expense has been deleted successfully!"
            }))
        else:
            abort(500)
    except Exception as err:
        app.logger.error("Exception in expense delete: %s", err)
        abort(500)
