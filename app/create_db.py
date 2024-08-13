import sys
import os
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import mysql.connector

Base = declarative_base()

class Config(object):

    def __init__(self):
        try:
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            config = configparser.ConfigParser()

            config.read(os.path.join(path, 'config.ini'))

            self.DB_HOST = config.get('DEFAULT', 'dbhost', fallback='')
            self.DB_NAME = config.get('DEFAULT', 'dbname', fallback='')
            self.DB_USER = config.get('DEFAULT', 'dbuser', fallback='')
            self.DB_PASSWORD = config.get('DEFAULT', 'dbpassword', fallback='')

            connection_string = (
                'mysql+mysqlconnector://{}:{}@{}/{}?charset=utf8&auth_plugin=mysql_native_password'
                .format(self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME)
            )

            self.engine = create_engine(connection_string, echo=False)
            self.session = sessionmaker(bind=self.engine)

        except mysql.connector.Error as err:

            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                self.erro = 1  # Erro User e Senha

            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                mydb = mysql.connector.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD,)
                my_cursor = mydb.cursor()
                my_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.DB_NAME}")


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