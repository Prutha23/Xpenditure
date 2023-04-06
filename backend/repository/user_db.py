from repository import db_connect
from main import app


class UserDB:
    def __int__(self):
        pass

    def get_user_from_username(self, username):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"SELECT ID, USERNAME, PASSWORD, ROLE, IS_ACTIVE FROM USERS WHERE USERNAME = '{username}'"
            app.logger.info(query)

            cursor.execute(query)
            user_dir = {}
            for row in cursor.fetchall():
                user_dir["ID"], user_dir["username"], user_dir["password"], user_dir["role"], user_dir[
                    "is_active"] = row
            return user_dir
        except Exception as err:
            app.logger.error("Exception in get_user_from_username %s", err)
            return None

    def add_user(self, username, password):
        try:
            return None
        except Exception as err:
            app.logger.error("Exception in add_user %s", err)
            return None

    def delete_user(self, username):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"DELETE FROM USERS WHERE USERNAME = '{username}';"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)

            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in delete_user %s", err)
            return None
