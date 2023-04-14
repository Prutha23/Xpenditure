from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import expense_db
from utils.auth import admin_required, abort

# Get All Expenses Report
@app.route("/api/reports/expenses", methods=["GET"])
@admin_required
def get_all_expenses():
    try:
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

# Get Top Expenses
@app.route("/api/reports/topexpenses", methods=["GET"])
@admin_required
def get_top_expenses():
    try:
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

# Get All Expense by Category Report
@app.route("/api/reports/expensesbycategory", methods=["GET"])
@admin_required
def get_expenses_by_category():
    try:
        # cat_id
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

# Get Top Users by Expenses
@app.route("/api/reports/topusers", methods=["GET"])
@admin_required
def get_top_users_by_expenses():
    try:
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

# Get Average Expenses per User
@app.route("/api/reports/expensesperuse", methods=["GET"])
@admin_required
def get_average_expenses_per_user():
    try:
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

# Get Average Expenses per User
@app.route("/api/reports/avgexpensebyusers", methods=["GET"])
@admin_required
def get_expense_by_user_type():
    try:
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