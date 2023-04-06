from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import category_db
from utils.auth import auth_required, admin_required, abort, get_current_user, check_is_premium


@app.route("/api/category/getAllForAdmin")
@admin_required
def get_all_categories():
    try:
        obj = category_db.CategoryDB()
        res = obj.get_all_categories()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in getAllForAdmin: %s", err)
        abort(500)


@app.route("/api/category/getAllForCurrentUser")
@auth_required
def get_categories_for_user():
    try:
        obj = category_db.CategoryDB()
        res = obj.get_categories_for_user()
        if res:
            return make_response(jsonify({
                "statusCode": 200,
                "status": "Success",
                "message": "Success",
                "data": res
            }))
    except Exception as err:
        app.logger.error("Exception in getAllForCurrentUser: %s", err)
        abort(500)


@app.route("/api/category/addCategory", methods=['POST'])
@auth_required
def add_category():
    try:
        # name, remarks
        user = get_current_user()
        is_premium = check_is_premium()

        if user["role"] == 2 or is_premium == 1:
            data = request.get_json()
            obj = category_db.CategoryDB()
            res = obj.add_category(user["ID"], data["name"], data["remarks"])
            if res:
                return make_response(jsonify({
                    "statusCode": 200,
                    "status": "Success",
                    "message": "Category has been added successfully!"
                }))
            else:
                abort(500)
        else:
            abort(403)
    except Exception as err:
        app.logger.error("Exception in category add: ", err)
        abort(500)


@app.route("/api/category/editCategory", methods=['POST'])
@auth_required
def update_category():
    try:
        # id, name, remarks
        user = get_current_user()
        is_premium = check_is_premium()

        if user["role"] == 2 or is_premium == 1:
            data = request.get_json()
            obj = category_db.CategoryDB()
            res = obj.update_category(user["role"], user["ID"], data["id"], data["name"], data["remarks"])
            if res:
                return make_response(jsonify({
                    "statusCode": 200,
                    "status": "Success",
                    "message": "Category has been updated successfully!"
                }))
            else:
                abort(500)
        else:
            abort(403)
    except Exception as err:
        app.logger.error("Exception in category update: %s", err)
        abort(500)


@app.route("/api/category/deleteCategory", methods=['POST'])
@auth_required
def delete_category():
    try:
        # id
        user = get_current_user()
        is_premium = check_is_premium()

        if user["role"] == 2 or is_premium:
            data = request.get_json()
            obj = category_db.CategoryDB()
            res = obj.delete_category(user["role"], user["ID"], data["id"])
            if res:
                return make_response(jsonify({
                    "statusCode": 200,
                    "status": "Success",
                    "message": "Category has been deleted successfully!"
                }))
            else:
                abort(500)
        else:
            abort(403)
    except Exception as err:
        app.logger.error("Exception in category delete: %s", err)
        abort(500)
