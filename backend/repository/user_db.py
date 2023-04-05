from repository import db_connect


class UserDB:

    def __int__(self):
        pass

    def get_user_from_username(self, username):
        conn = db_connect.get_connection()
        cursor = conn.cursor()

        query = f"SELECT ID, USERNAME, PASSWORD, ROLE, IS_ACTIVE FROM USERS WHERE USERNAME = '{username}'"
        try:
            cursor.execute(query)
            user_dir = {}
            for row in cursor.fetchall():
                user_dir["ID"], user_dir["username"], user_dir["password"], user_dir["role"], user_dir[
                    "is_active"] = row
            if user_dir:
                print(user_dir)
            else:
                print("No result found")
            return user_dir

        except:
            print("exception")

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


# db = UserDB()
# result_user_data = db.get_user_from_username('prutha@gmail.com')
# res = db.delete_user('zarna@gmail.com')
# print(res)
