from repository import db_connect
from utils import auth
from main import app


class CategoryDB:

    def __int__(self):
        pass

    def get_all_categories(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()
            category_list = []

            query = f"select ID, NAME, REMARKS from CATEGORY;"
            app.logger.info(query)

            cursor.execute(query)
            for row in cursor.fetchall():
                category_dit = {}
                category_dit["ID"], category_dit["NAME"], category_dit["REMARKS"] = row
                category_list.append(category_dit)
            return category_list
        except Exception as err:
            app.logger.error("Exception in get_all_categories: %s", err)
            return None

    def get_categories_for_user(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()
            category_list = []

            query = f"select ID, NAME, REMARKS from CATEGORY where created_by = '{user_id}' or created_by IN (select ID from users where role = 5);"
            app.logger.info(query)

            cursor.execute(query)
            for row in cursor.fetchall():
                category_dit = {}
                category_dit["ID"], category_dit["NAME"], category_dit["REMARKS"] = row
                category_list.append(category_dit)
            return category_list
        except Exception as err:
            app.logger.error("Exception in get_categories_for_user: %s", err)
            return None

    def add_category(self, user_id, name, remarks):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"INSERT INTO CATEGORY(NAME, REMARKS, CREATED_BY) VALUES ('{name}','{remarks}','{user_id}'); "
            app.logger.info(query)

            cursor.execute(query)
            cursor.commit()
            return True
        except Exception as err:
            app.logger.error("Exception in add_category: %s", err)
            return None

    def update_category(self, role, user_id, cat_id, name, remarks):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            if role == 2:
                query = f"UPDATE CATEGORY SET NAME = '{name}', REMARKS = '{remarks}', UPDATED_BY = '{user_id}' WHERE ID = '{cat_id}';"
            else:
                query = f"UPDATE CATEGORY SET NAME = '{name}', REMARKS = '{remarks}', UPDATED_BY = '{user_id}' WHERE ID = '{cat_id}' and created_by = '{user_id}';"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)

            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Unable to update category: %s", err)
            return None

    def delete_category(self, role, user_id, cat_id):
        try:
            if role == 2:
                query = f"DELETE FROM CATEGORY WHERE id = '{cat_id}';"
            else:
                query = f"DELETE FROM CATEGORY WHERE id = '{cat_id}' and created_by = '{user_id}';"
            app.logger.info(query)

            conn = db_connect.get_connection()
            cursor = conn.cursor()

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in delete_category: %s", err)
            return None
