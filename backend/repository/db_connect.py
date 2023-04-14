import pyodbc as odbc


def get_connection():
    return odbc.connect('DRIVER={SQL Server};SERVER=Urvil\MSSQLSERVER2K23;DATABASE=Xpenditure;')
