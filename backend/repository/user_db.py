from repository import db_connect
from main import app
from utils import auth


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
            app.logger.error("Exception in get_user_from_username: %s", err)
            return None

    def get_is_premium(self, username):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"SELECT is_premium FROM USERS_DETAILS WHERE U_ID IN (select id from users where username = '{username}');"
            app.logger.info(query)

            cursor.execute(query)
            for row in cursor.fetchall():
                if row[0] == 1:
                    return True
                else:
                    return False
        except Exception as err:
            app.logger.error("Exception in get_is_premium: %s", err)
            return None

    def update_user_password(self, userId, password):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"UPDATE USERS SET PASSWORD = '{password}' where ID = '{userId}';"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True

        except Exception as err:
            app.logger.error("Exception in delete_user: %s", err)
            return None

    def add_user(self, username, password, fname, lname, phoneno, addressline1, street, province, zipcode, country):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"INSERT into USERS(USERNAME, PASSWORD, ROLE, IS_ACTIVE) VALUES('{username}', '{password}', 1, 1);"
            app.logger.info(query)

            cursor.insert_id()

        except Exception as err:
            app.logger.error("Exception in add_user: %s", err)
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
            app.logger.error("Exception in delete_user: %s", err)
            return None

    def get_user_details_from_user_id(self, userId):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"SELECT U_ID, FNAME, LNAME, EMAILID, PHONENO, ADDRESSLINE1, STREET, PROVINCE, ZIPCODE, COUNTRY, IS_PREMIUM FROM USERS_DETAILS WHERE U_ID = '{userId}';"
            app.logger.info(query)

            cursor.execute(query)
            user_detail_dir = {}
            for row in cursor.fetchall():
                user_detail_dir["U_ID"], user_detail_dir["fname"], user_detail_dir["lname"], user_detail_dir["emailid"], \
                user_detail_dir["phoneno"], user_detail_dir["addressline1"], user_detail_dir["street"], user_detail_dir["province"], \
                user_detail_dir["zipcode"], user_detail_dir["country"], user_detail_dir["is_premium"] = row

            return user_detail_dir
        except Exception as err:
            app.logger.error("Exception in get_user_details_from_user_id: %s", err)
            return None

    def update_user_details(self, id, fname, lname, phoneno, addressline1, street, province, zipcode, country):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"UPDATE USERS_DETAILS SET FNAME = '{fname}', LNAME = '{lname}', PHONENO = '{phoneno}', ADDRESSLINE1 = '{addressline1}', STREET = '{street}', PROVINCE = '{province}', ZIPCODE = '{zipcode}', COUNTRY = '{country}', UPDATED_BY = '{user_id}' WHERE U_ID = '{id};"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in update_user_details: %s", err)
            return None
