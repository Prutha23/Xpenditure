from repository import db_connect
from main import app
from utils import auth


class SubscriptionDB:
    def __int__(self):
        pass

    def receive_payment(self, PAYMENT_METHOD, CARD_HOLDER_NAME, CARD_NO, END_DATE):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"INSERT INTO PAYMENT(USERID, PAYMENT_METHOD, AMOUNT, CARD_HOLDER_NAME, CARD_NO, PAYMENT_STATUS, SUBSRIPTION_DATE, END_DATE) VALUES('{user_id}', '{PAYMENT_METHOD}', 29, '{CARD_HOLDER_NAME}', '{CARD_NO}', 'p', getdate(), '{END_DATE}');"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in receive_payment: %s", err)
            return None

    def approve_payment(self, u_id, start_date, end_date):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()
            user_id = auth.get_current_user_id()

            query = f"UPDATE PAYMENT SET PAYMENT_STATUS = 'a', UPDATED_BY = '{user_id}', UPDATED_DATE = getdate() WHERE USERID = '{u_id}';"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount != 0:
                cursor = conn.cursor()
                query = f"exec APPROVE_PAYMENT @id='{u_id}', @uid='{user_id}', @start_date='{start_date}', @end_date='{end_date}';"
                app.logger.info(query)

                cursor.execute(query)
                app.logger.info(cursor.rowcount)
                if cursor.rowcount != 0:

                    cursor = conn.cursor()
                    query = f"UPDATE USERS_DETAILS SET IS_PREMIUM = 1, UPDATED_BY = '{user_id}', UPDATED_DATE = getdate() WHERE U_ID = '{u_id}';"
                    app.logger.info(query)

                    cursor.execute(query)
                    app.logger.info(cursor.rowcount)
                    if cursor.rowcount != 0:
                        conn.commit()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                conn.commit()
                return False
        except Exception as err:
            app.logger.error("Exception in receive_payment: %s", err)
            return None

    def get_payment_details(self, user_id):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"select SUBSRIPTION_DATE, END_DATE, AMOUNT from payment where userid= '{user_id}' and PAYMENT_STATUS = 'p'"
            app.logger.info(query)

            cursor.execute(query)
            pay_dict = {}
            for row in cursor.fetchall():
                pay_dict["SUBSRIPTION_DATE"], pay_dict["END_DATE"], pay_dict["AMOUNT"] = row
            return pay_dict
        except Exception as err:
            app.logger.error("Exception in get_payment_details: %s", err)
            return None
