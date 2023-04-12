from repository import db_connect
from utils import auth
from main import app


class ReminderDB:

    def __int__(self):
        pass

    def getall_for_current_user(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()
            reminder_list = []

            query = f"select ID, EMAIL, DUE_DATE, DESCRIPTION from NOTIFICATION where U_ID = '{user_id}' ORDER BY DUE_DATE DESC;"
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                reminder_dit = {}
                reminder_dit["ID"], reminder_dit["EMAIL"], reminder_dit["DUE_DATE"], reminder_dit["DESCRIPTION"] = row
                reminder_list.append(reminder_dit)
            return reminder_list
        except Exception as err:
            app.logger.error("Exception in getall_for_current_user %s", err)
            return None

    def add_reminder(self, email, due_date, description):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"INSERT INTO NOTIFICATION(U_ID, EMAIL, DUE_DATE, DESCRIPTION, CREATED_BY) VALUES ('{user_id}','{email}','{due_date}','{description}', '{user_id}');"
            app.logger.info(query)

            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in add_reminder %s", err)
            return None

    def update_reminder(self, r_id, email, due_date, description):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"UPDATE NOTIFICATION SET EMAIL = '{email}', DESCRIPTION = '{description}', UPDATED_BY = '{user_id}', DUE_DATE = '{due_date}' WHERE ID = '{r_id}' and created_by = '{user_id}';"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Unable to update_reminder %s", err)
            return None

    def delete_reminder(self, r_id):
        try:
            user_id = auth.get_current_user_id()
            query = f"DELETE FROM NOTIFICATION WHERE ID = '{r_id}' and created_by = '{user_id}';"
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
            app.logger.error("Exception in delete_reminder %s", err)
            return None
