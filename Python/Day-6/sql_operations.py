"""Importing modules"""
import mysql.connector
from mysql.connector import errorcode
import dbconfig as cfg


class DbConnect:
    """Defines methods to connect and disconnect to DB"""

    def __init__(self):
        """Initializes variables and Reads DB Credentials from dbconfig file to config file"""
        self.config = {'host': cfg.mysql["host"],
                       'user': cfg.mysql["user"],
                       'password': cfg.mysql["password"],
                       'database': cfg.mysql["database"]
                       }
        self.cnx = ''

    def connect(self):
        """Attempts to connect to DB using credentials from dbconfig file"""
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        """Disconnects to Db"""
        self.cnx.close()


if __name__ == '__main__':
    obj = DbConnect()
    obj.connect()
    obj.disconnect()
