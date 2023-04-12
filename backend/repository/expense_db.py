from repository import db_connect
from utils import auth
from main import app


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