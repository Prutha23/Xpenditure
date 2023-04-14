from repository import db_connect
from main import app
from utils import auth


class UserDetailsDB:
    def __int__(self):
        pass

    def register(self, username, password, fname, lname, phoneno, addressline1, street, province, zipcode, country):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"INSERT into USERS(USERNAME, PASSWORD, ROLE, IS_ACTIVE) VALUES('{username}', '{password}', 1, 1);"
            app.logger.info(query)
            cursor.execute(query)
            u_id = 0

            if cursor.rowcount != 0:
                cursor = conn.cursor()
                query = f"SELECT ID from USERS where username='{username}'"
                app.logger.info(query)
                cursor.execute(query)

                for row in cursor.fetchall():
                    u_id = row[0]
                app.logger.info(u_id)

                if u_id != 0:
                    cursor = conn.cursor()
                    query = f"INSERT into USERS_DETAILS(FNAME, LNAME, EMAILID, IS_PREMIUM, PHONENO, ADDRESSLINE1, STREET, PROVINCE, ZIPCODE, COUNTRY, U_ID) VALUES('{fname}', '{lname}', '{username}', 0,'{phoneno}','{addressline1}','{street}','{province}','{zipcode}','{country}','{u_id}')";
                    app.logger.info(query)
                    cursor.execute(query)

                    if cursor.rowcount != 0:
                        conn.commit()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except Exception as err:
            app.logger.error("Exception in add_user: %s", err)
            return None

    def get_user_details_from_user_id(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            userId = auth.get_current_user_id()

            query = f"SELECT U_ID, FNAME, LNAME, EMAILID, PHONENO, ADDRESSLINE1, STREET, PROVINCE, ZIPCODE, COUNTRY FROM USERS_DETAILS WHERE U_ID = '{userId}';"
            app.logger.info(query)

            cursor.execute(query)
            user_detail_dir = {}
            for row in cursor.fetchall():
                user_detail_dir["U_ID"], user_detail_dir["FNAME"], user_detail_dir["LNAME"], user_detail_dir["EMAILID"], \
                user_detail_dir["PHONENO"], user_detail_dir["ADDRESSLINE1"], user_detail_dir["STREET"], user_detail_dir["PROVINCE"], \
                user_detail_dir["ZIPCODE"], user_detail_dir["COUNTRY"] = row

            return user_detail_dir
        except Exception as err:
            app.logger.error("Exception in get_user_details_from_user_id: %s", err)
            return None

    def update_user_details(self, id, fname, lname, phoneno, addressline1, street, province, zipcode, country):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"UPDATE USERS_DETAILS SET FNAME = '{fname}', LNAME = '{lname}', PHONENO = '{phoneno}', ADDRESSLINE1 = '{addressline1}', STREET = '{street}', PROVINCE = '{province}', ZIPCODE = '{zipcode}', COUNTRY = '{country}', UPDATED_BY = '{user_id}' WHERE U_ID = '{id}';"
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
