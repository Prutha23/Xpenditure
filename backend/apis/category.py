from flask import request, make_response
from flask.json import jsonify
from main import app
from repository import category_db
from utils.auth import auth_required, admin_required, abort, get_current_user, check_is_premium


@app.route("/api/category/getAllForAdmin")
@admin_required
def get_all_categories():
    try:
        """
            It will return all the default categories created by admins 
            it requires admin access because only admin can do CRUD on these default categories
        """
        obj = category_db.CategoryDB()
        res = obj.get_all_categories()
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
        app.logger.error("Exception in getAllForAdmin: %s", err)
        abort(500)


@app.route("/api/category/getAllForCurrentUser")
@auth_required
def get_categories_for_user():
    try:
        """
            this api used is to fetch all categories to show in expense form dropdown menu
        """
        obj = category_db.CategoryDB()
        res = obj.get_categories_for_user()
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


@app.route("/api/category/getAllPremiumCategories")
@auth_required
def get_all_premium_categories_for_user():
    try:
        """
            this api used is to fetch all categories to show in expense form dropdown menu
        """
        obj = category_db.CategoryDB()
        res = obj.get_premium_categories_for_user()
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
        app.logger.error("Exception in get_all_premium_categories_for_user: %s", err)
        abort(500)


@app.route("/api/category/addCategory", methods=['POST'])
@auth_required
def add_category():
    try:
        """
            this api is used to add the category into Category table 
            Note: only admin and premium users can do this
            request param: NAME, REMARKS
        """
        user = get_current_user()
        is_premium = check_is_premium()

        if user["role"] == 2 or is_premium == 1:
            data = request.get_json()
            obj = category_db.CategoryDB()
            res = obj.add_category(user["ID"], data["NAME"], data["REMARKS"])
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
        """
            this api is used to update the already created category
            request param: ID, NAME, REMARKS
        """
        user = get_current_user()
        is_premium = check_is_premium()

        if user["role"] == 2 or is_premium == 1:
            data = request.get_json()
            obj = category_db.CategoryDB()
            res = obj.update_category(user["role"], user["ID"], data["ID"], data["NAME"], data["REMARKS"])
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


"""
    as delete category is not permitted to any type of users, we have commented this method
"""
# @app.route("/api/category/deleteCategory", methods=['POST'])
# @auth_required
# def delete_category():
#     try:
#         # id
#         user = get_current_user()
#         is_premium = check_is_premium()
#
#         if user["role"] == 2 or is_premium:
#             data = request.get_json()
#             obj = category_db.CategoryDB()
#             res = obj.delete_category(user["role"], user["ID"], data["id"])
#             if res:
#                 return make_response(jsonify({
#                     "statusCode": 200,
#                     "status": "Success",
#                     "message": "Category has been deleted successfully!"
#                 }))
#             else:
#                 abort(500)
#         else:
#             abort(403)
#     except Exception as err:
#         app.logger.error("Exception in category delete: %s", err)
#         abort(500)
