from repository import db_connect
from main import app
from utils import auth


class UserDB:
    def __int__(self):
        pass

    def get_all(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"SELECT u.ID, u.USERNAME, u.IS_ACTIVE, ud.IS_PREMIUM FROM USERS u LEFT JOIN USERS_DETAILS ud ON u.ID = ud.U_ID ORDER BY USERNAME"
            app.logger.info(query)
            users = []

            cursor.execute(query)
            for row in cursor.fetchall():
                user_dir = {}
                user_dir["ID"], user_dir["USERNAME"], user_dir["IS_ACTIVE"], user_dir["IS_PREMIUM"] = row
                users.append(user_dir)
            return users
        except Exception as err:
            app.logger.error("Exception in get_all: %s", err)
            return None

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
            app.logger.error("Exception in update_user_password: %s", err)
            return None

    def update_active_status(self, id, is_active):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"UPDATE USERS SET IS_ACTIVE = '{is_active}' where ID = '{id}';"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in update_active_status: %s", err)
            return None

    def get_user_dashboard_data(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"select c.NAME, sum(e.AMOUNT) from EXPENSE e LEFT JOIN CATEGORY c ON c.ID = e.CAT_ID where e.CREATED_BY = '{user_id}' and e.EXPENSE_DATE between cast(DATEADD(mm, DATEDIFF(m,0,GETDATE()),0) as date) and cast(DATEADD(s,-1,DATEADD(mm, DATEDIFF(m,0,GETDATE())+1,0)) as date) group by c.NAME ORDER BY c.NAME;"
            app.logger.info(query)

            cursor.execute(query)
            data = []
            for row in cursor.fetchall():
                dir = {}
                dir["NAME"], dir["TOTAL"] = row
                data.append(dir)
            return data
        except Exception as err:
            app.logger.error("Exception in get_user_dashboard_data: %s", err)
            return None

    def get_admin_dashboard_data(self):
        try:
            conn = db_connect.get_connection()
            dir = {}

            cursor = conn.cursor()
            query = f"select count(*) as no from USERS where IS_ACTIVE=1;"
            app.logger.info(query)
            cursor.execute(query)
            for row in cursor.fetchall():
                dir["USERS"] = row[0]

            cursor = conn.cursor()
            query = f"select count(*) as no from USERS_DETAILS where IS_PREMIUM=1;"
            app.logger.info(query)
            cursor.execute(query)
            for row in cursor.fetchall():
                dir["PREMIUM_USERS"] = row[0]

            cursor = conn.cursor()
            query = f"select c.NAME, sum(e.AMOUNT) from EXPENSE e LEFT JOIN CATEGORY c ON c.ID = e.CAT_ID where e.EXPENSE_DATE between cast(DATEADD(mm, DATEDIFF(m,0,GETDATE()),0) as date) and cast(DATEADD(s,-1,DATEADD(mm, DATEDIFF(m,0,GETDATE())+1,0)) as date) group by c.NAME ORDER BY c.NAME;"
            app.logger.info(query)
            cursor.execute(query)
            expenses = []
            for row in cursor.fetchall():
                data = {}
                data["NAME"], data["TOTAL"] = row
                expenses.append(data)
            dir["EXPENSES"] = expenses
            return dir
        except Exception as err:
            app.logger.error("Exception in get_admin_counts: %s", err)
            return None

    # def delete_user(self, username):
    #     try:
    #         conn = db_connect.get_connection()
    #         cursor = conn.cursor()
    #
    #         query = f"DELETE FROM USERS WHERE USERNAME = '{username}';"
    #         app.logger.info(query)
    #
    #         cursor.execute(query)
    #         app.logger.info(cursor.rowcount)
    #
    #         if cursor.rowcount == 0:
    #             return False
    #         else:
    #             conn.commit()
    #             return True
    #     except Exception as err:
    #         app.logger.error("Exception in delete_user: %s", err)
    #         return None
