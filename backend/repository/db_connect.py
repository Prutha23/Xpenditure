import pyodbc as odbc


def get_connection():
    return odbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-K37RBTK\GSQL;DATABASE=Xpenditure;')
