from flask import request, make_response
from main import app
from repository import expense_db
from flask.json import jsonify


@app.route("/api/expenseByCategoryId")
def demo():
    cat_id = request.json.get('cat_id', None)
    obj = expense_db.ExpenseDB()
    return make_response(jsonify(
        obj.get_expense_from_category_id(cat_id)
    ))
