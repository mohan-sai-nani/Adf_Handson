"""Importing modules"""
import datetime
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
        self.mycursor = ''

    def connect(self):
        """Attempts to connect to DB using credentials from dbconfig file"""
        try:
            self.cnx = mysql.connector.connect(**self.config)
            self.mycursor = self.cnx.cursor()
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


class DbOperations(DbConnect):
    """Reads Data from Users"""

    def __init__(self, inp):
        """Initializes data"""
        super().__init__()
        super().connect()
        self.userdata = inp

    def insert_data(self):
        """Inserts data into DB"""
        sql = "INSERT INTO REQUEST_INFO (FIRST_NAME, MIDDLE_NAME, LAST_NAME, DOB, GENDER, NATIONALITY, CURRENT_CITY, STATE, PIN_CODE, QUALIFICATION, SALARY, PAN_NUMBER) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        first_name, middle_name, last_name, dob, gender, nationality, current_city, state, pin_code, qualification, salary, pan_number = self.userdata
        values = (first_name, middle_name, last_name, dob, gender, nationality, current_city, state, pin_code, qualification, salary, pan_number)
        self.mycursor.execute(sql, values)
        self.cnx.commit()


def mandate_inp(text, typ):
    """Reads input fields which are mandatory from user"""
    print(text)
    inp = ''
    # 1- Str, 2- int, 3- Date, 4- M/F, 5- not mandatory
    if typ == 1:
        try:
            inp = str(input())
        except ValueError:
            print("Invalid Input! Required String")
            inp = mandate_inp(text, typ)
    if typ == 2:
        try:
            inp = int(input())
        except ValueError:
            print("Invalid Input! Required Number")
            inp = mandate_inp(text, typ)
    if typ == 3:
        try:
            required = "%Y-%m-%d"
            inp = str(input())
            if not datetime.datetime.strptime(inp, required):
                print("Incorrect Date. Format should be: YYYY-MM-DD")
                inp = mandate_inp(text, required)
        except ValueError:
            print("Invalid Input! Required Date (YYYY-MM-DD)")
            inp = mandate_inp(text, typ)
    if typ == 4:
        try:
            inp = str(input())
            while inp not in ('M', 'F', 'm', 'f'):
                print("Input should be (M / F)")
                print(text)
                inp = str(input())
        except ValueError:
            print("Invalid Input! Required (M / F)")
            inp = mandate_inp(text, typ)
    if typ == 5:
        inp = str(input())
        return inp
    if inp == '':
        print("This is a mandatory field")
        inp = mandate_inp(text, typ)
    return inp


if __name__ == '__main__':
    # 1- Str, 2- int, 3- Date, 4- M/F, 5- not mandatory
    print("Please provide the following details, fields marked as * are mandatory")
    fields = ["First Name*: ", 1,
              "Middle Name: ", 5,
              "Last Name*: ", 1,
              "DOB(YYYY-MM-DD)*: ", 3,
              "Gender(M/F)*: ", 4,
              "Nationality*: ", 1,
              "Current City*: ", 1,
              "State*: ", 1,
              "Pin-code*: ", 2,
              "Qualification*: ", 1,
              "Salary*: ", 2,
              "PAN Number*: ", 1
              ]
    data = []
    for i in range(0, len(fields), 2):
        data.append(mandate_inp(fields[i], fields[i+1]))
    dbobj2 = DbOperations(data)
    dbobj2.insert_data()
