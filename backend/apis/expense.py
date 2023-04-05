from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import expense_db
from utils.auth import auth_required, abort


@app.route("/api/expense/getByCategoryId")
@auth_required
def get_by_category_id():
    try:
        # cat_id = request.json.get('cat_id', None)
        args = request.args.to_dict()
        obj = expense_db.ExpenseDB()
        return make_response(jsonify(
            obj.get_expense_from_category_id(args["cat_id"])
        ))
    except:
        abort(500)
