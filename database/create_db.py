import sys
import os
import configparser
import mysql.connector


path = os.path.abspath(os.path.dirname(sys.argv[0]))
config = configparser.ConfigParser()
config.read(os.path.join(path, 'config.ini'))

DB_HOST = config.get('DEFAULT', 'dbhost', fallback='')
DB_NAME = config.get('DEFAULT', 'dbname', fallback='')
DB_USER = config.get('DEFAULT', 'dbuser', fallback='')
DB_PASSWORD = config.get('DEFAULT', 'dbpassword', fallback='')

mydb = mysql.connector.connect(
    host = DB_HOST, 
    user = DB_USER,
    passwd = DB_PASSWORD,
    )

my_cursor = mydb.cursor()
my_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")