import pyodbc as odbc


def get_connection():
    return odbc.connect('DRIVER={SQL Server};SERVER=Prutha\MSSQLSERVER_P;DATABASE=Xpenditure;')
