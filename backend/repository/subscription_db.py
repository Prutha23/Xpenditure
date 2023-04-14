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

    def check_payment_status(self, user_id):
        try:
            conn = db_connect.get_connection()
            cursor = conn.cursor()

            query = f"select ID from payment where userid= '{user_id}' and PAYMENT_STATUS = 'p'"
            app.logger.info(query)

            cursor.execute(query)
            app.logger.info(cursor.rowcount)
            if cursor.rowcount == 0:
                return False
            else:
                conn.commit()
                return True
        except Exception as err:
            app.logger.error("Exception in check_payment_status: %s", err)
            return None
