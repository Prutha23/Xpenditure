from repository import db_connect
from utils import auth
from main import app
import pandas as pd


class ExpenseDB:

    def __int__(self):
        pass

    def getall_expenses_for_current_user(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()
            expense_list = []

            query = f"select e.ID, c.NAME, e.AMOUNT, e.DESCRIPTION, e.EXPENSE_DATE from EXPENSE e LEFT JOIN CATEGORY c ON e.CAT_ID = c.ID where e.created_by = '{user_id}' ORDER BY e.EXPENSE_DATE DESC;"
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                expense_dit = {}
                expense_dit["ID"], expense_dit["NAME"], expense_dit["AMOUNT"], expense_dit["DESCRIPTION"], expense_dit["EXPENSE_DATE"] = row
                expense_list.append(expense_dit)
            return expense_list
        except Exception as err:
            app.logger.error("Exception in getall_expenses_for_current_user %s", err)
            return None

    def get_expense_from_category_id(self, catid):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()
            expense_list = []

            query = f"select ID, CAT_ID, EXPENSE_DATE, AMOUNT, DESCRIPTION from EXPENSE where CAT_ID = '{catid}' and created_by = '{user_id}' ORDER BY EXPENSE_DATE DESC;"
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                expense_dit = {}
                expense_dit["ID"], expense_dit["CAT_ID"], expense_dit["EXPENSE_DATE"], expense_dit["AMOUNT"], expense_dit["DESCRIPTION"] = row
                expense_list.append(expense_dit)
            return expense_list
        except Exception as err:
            app.logger.error("Exception in get_expense_from_category_id %s", err)
            return None

    def add_expense(self, cat_id, amount, description, expense_date):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"INSERT INTO EXPENSE(CAT_ID, AMOUNT, CREATED_BY, DESCRIPTION, EXPENSE_DATE) VALUES ('{cat_id}','{amount}','{user_id}','{description}','{expense_date}'); "
            app.logger.info(query)

            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in add_expense %s", err)
            return None

    def update_expense(self, expense_id, cat_id, amount, description, expense_date):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"UPDATE EXPENSE SET CAT_ID = '{cat_id}', AMOUNT = '{amount}', DESCRIPTION = '{description}', UPDATED_BY = '{user_id}', expense_date = '{expense_date}' WHERE ID = '{expense_id}' and created_by = '{user_id}';"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Unable to update the data %s", err)
            return None

    def delete_expense(self, exp_id):
        try:
            user_id = auth.get_current_user_id()
            query = f"DELETE FROM EXPENSE WHERE id = '{exp_id}' and created_by = '{user_id}';"
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
            app.logger.error("Exception in delete_expense %s", err)
            return None

    # Repository functions for Report and Expense Prediction API
    # Get All Expenses Report
    def get_all_expenses(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            expense_list = []

            query = "SELECT ID, CAT_ID, AMOUNT, CREATED_BY, DESCRIPTION, CREATED_DATE, UPDATED_BY, UPDATED_DATE, EXPENSE_DATE FROM EXPENSE  "
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                expense_dit = {}
                (expense_dit["ID"], expense_dit["CAT_ID"], expense_dit["AMOUNT"], expense_dit["CREATED_BY"],
                 expense_dit["DESCRIPTION"], expense_dit["CREATED_DATE"], expense_dit["UPDATED_BY"],
                 expense_dit["UPDATED_DATE"], expense_dit["EXPENSE_DATE"]) = row
                expense_list.append(expense_dit)
                return expense_list
        except Exception as err:
            app.logger.error("Exception in Get All Expenses Function %s", err)
            return None

    # Get Top Expenses Report
    def get_top_expenses(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            expense_list = []

            query = "SELECT ID, CAT_ID, AMOUNT, CREATED_BY, DESCRIPTION, CREATED_DATE, UPDATED_BY, UPDATED_DATE, EXPENSE_DATE FROM EXPENSE  "
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                expense_dit = {}
                expense_dit["ID"], expense_dit["CAT_ID"], expense_dit["AMOUNT"] = row
                expense_list.append(expense_dit)
                return expense_list
        except Exception as err:
            app.logger.error("Exception in Get Top Expenses Function %s", err)
            return None

    # Get All Expense by Category Report
    def get_expenses_by_category(self, category_id):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            expense_list = []

            query = f"SELECT ID, CAT_ID, AMOUNT FROM EXPENSE WHERE CAT_ID = {category_id}"
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                expense_dict = {}
                expense_dict["ID"], expense_dict["CAT_ID"], expense_dict["AMOUNT"] = row
                expense_list.append(expense_dict)
            return expense_list
        except Exception as err:
            app.logger.error("Exception in Get All Expense by Category Report %s", err)
            return None

    # Get Top Users by Expenses
    def get_top_users_by_expenses(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            top_users_list = []

            query = """
                SELECT TOP 10
                    U.ID,
                    U.USERNAME,
                SUM(E.AMOUNT) AS TOTAL_EXPENSE
                    FROM
                    USERS U
                JOIN
                    EXPENSE E ON E.CREATED_BY = U.ID
                GROUP BY
                    U.ID, U.USERNAME
                ORDER BY
                    TOTAL_EXPENSE DESC;
            """
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                user_dit = {}
                user_dit["ID"], user_dit["USERNAME"], user_dit["TOTAL_EXPENSE"] = row
                top_users_list.append(user_dit)
            return top_users_list
        except Exception as err:
            app.logger.error("Exception in Get Top Users by Expenses %s", err)
            return None

    # Get Average Expenses per User
    def get_average_expenses_per_user(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_expense_list = []

            query = """SELECT U.ID AS USER_ID, U.USERNAME, AVG(E.AMOUNT) AS AVG_EXPENSE
                    FROM USERS U
                    JOIN EXPENSE E ON U.ID = E.CREATED_BY
                    GROUP BY U.ID, U.USERNAME;"""
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                user_expense_dict = {}
                user_expense_dict["USER_ID"], user_expense_dict["USERNAME"], user_expense_dict["AVG_EXPENSE"] = row
                user_expense_list.append(user_expense_dict)
            return user_expense_list
        except Exception as err:
            app.logger.error("Exception in Get Average Expenses per User %s", err)
            return None

    # Get Expense by User Type
    def get_expense_by_user_type(self):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_expense_list = []

            query = """
                SELECT 
                    U.ID AS USER_ID,
                    CASE
                        WHEN PU.ID IS NULL THEN 'Regular User'
                        ELSE 'Premium User'
                    END AS USER_TYPE,
                    SUM(E.AMOUNT) AS TOTAL_EXPENSE
                FROM 
                    USERS U
                LEFT JOIN 
                    PREMIUM_USERS PU ON U.ID = PU.USERID
                INNER JOIN 
                    EXPENSE E ON U.ID = E.CREATED_BY
                GROUP BY 
                    U.ID,
                    PU.ID;
            """
            app.logger.info(query)
            cursor.execute(query)

            for row in cursor.fetchall():
                expense_dict = {}
                expense_dict["USER_ID"], expense_dict["USER_TYPE"], expense_dict["TOTAL_EXPENSE"] = row
                user_expense_list.append(expense_dict)

            return user_expense_list
        except Exception as err:
            app.logger.error("Exception in Get Expense by User Type %s", err)
            return None

    # Expense Data for Prediction "RETURNS CSV DATA FOR PREDICTION"
    def get_expense_data_for_prediction():
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = """
            SELECT
                E.ID AS Expense_ID,
                E.CAT_ID AS Category_ID,
                C.NAME AS Category_Name,
                E.AMOUNT AS Amount,
                E.CREATED_BY AS User_ID,
                UD.EMAILID AS User_Email,
                UD.IS_PREMIUM AS Is_Premium,
                E.EXPENSE_DATE AS Expense_Date
            FROM
                EXPENSE E
                INNER JOIN CATEGORY C ON E.CAT_ID = C.ID
                INNER JOIN USERS_DETAILS UD ON E.CREATED_BY = UD.U_ID;
            """
            cursor.execute(query)
            result = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            return pd.DataFrame(result, columns=column_names)
        except Exception as err:
            app.logger.error("Exception in get_expense_data_for_prediction: %s", err)
            return None

