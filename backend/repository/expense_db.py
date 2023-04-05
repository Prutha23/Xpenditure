from repository import db_connect
from utils import auth


class ExpenseDB:

    def __int__(self):
        pass

    def get_expense_from_category_id(self, catid):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()
            expense_list = []

            query = f"select ID, CAT_ID, AMOUNT, DESCRIPTION from EXPENSE where CAT_ID = '{catid}' and created_by = '{user_id}';"
            cursor.execute(query)

            for row in cursor.fetchall():
                expense_dit = {}
                expense_dit["ID"], expense_dit["CAT_ID"], expense_dit["AMOUNT"], expense_dit["DESCRIPTION"] = row
                expense_list.append(expense_dit)
            return expense_list
        except:
            print("exception")
            return None

    def add_user(self, username, password):
        pass

    def delete_user(self, username):

        query = f"DELETE FROM USERS WHERE USERNAME = '{username}';"
        conn = db_connect.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            print(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except:
            print("Exception while deleting the user-data")
