import sys
import os
import configparser

class Config:
    SQLALCHEMY_DATABASE_URI = (f"mysql+pymysql://root:comspirace@127.0.0.1:3306/crud_flask?charset=utf8")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
