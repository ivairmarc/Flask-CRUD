import mysql.connector


def create_db():
    mydb = mysql.connector.connect(
    host = '127.0.0.1', 
    user = 'root',
    passwd = 'comspirace',
    )

    my_cursor = mydb.cursor()
    my_cursor.execute(f"CREATE DATABASE IF NOT EXISTS digital_leads_dados")