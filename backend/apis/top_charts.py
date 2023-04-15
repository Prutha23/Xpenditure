from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import expense_db
from utils.auth import admin_required, abort


@app.route("/api/reports/expenses", methods=["GET"])
@admin_required
def get_all_expenses():
    try:
        """
            Get All Expenses Report
        """
        obj = expense_db.ExpenseDB()
        res = obj.get_all_expenses()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in all expenses: %s", err)
        abort(500)


@app.route("/api/reports/topexpenses", methods=["GET"])
@admin_required
def get_top_expenses():
    try:
        """
            Get Top Expenses
        """
        obj = expense_db.ExpenseDB()
        res = obj.get_top_expenses()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in all expenses: %s", err)
        abort(500)


@app.route("/api/reports/expensesbycategory", methods=["GET"])
@admin_required
def get_expenses_by_category():
    try:
        """
            Get All Expense by Category Report
            request param: category_id
        """
        args = request.args.to_dict()
        category_id = args.get('category_id')
        obj = expense_db.ExpenseDB()
        res = obj.get_expenses_by_category(category_id=category_id)
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in get_expenses_by_category: %s", err)
        abort(500)


@app.route("/api/reports/topusers", methods=["GET"])
@admin_required
def get_top_users_by_expenses():
    try:
        """
            Get Top Users by Expenses
        """
        obj = expense_db.ExpenseDB()
        res = obj.get_top_users_by_expenses()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in get_top_users_by_expenses : %s", err)
        abort(500)


@app.route("/api/reports/expensesperuse", methods=["GET"])
@admin_required
def get_average_expenses_per_user():
    try:
        """
            Get Average Expenses per User
        """
        obj = expense_db.ExpenseDB()
        res = obj.get_average_expenses_per_user()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in get_average_expenses_per_user : %s", err)
        abort(500)


@app.route("/api/reports/avgexpensebyusers", methods=["GET"])
@admin_required
def get_expense_by_user_type():
    try:
        """
            Get Average Expenses per User
        """
        obj = expense_db.ExpenseDB()
        res = obj.get_expense_by_user_type()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in get_expense_by_user_type : %s", err)
        abort(500)
