from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import expense_db
from utils.auth import admin_required, abort

@app.route("/api/reports/topexpenses", methods=["GET"])
@admin_required
def get_by_category_id():
    try:
        # cat_id
        args = request.args.to_dict()
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
        app.logger.error("Exception in top expenses: %s", err)
        abort(500)
