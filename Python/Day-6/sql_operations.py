"""Importing modules"""
import datetime
import logging
import mysql.connector
from mysql.connector import errorcode
import dbconfig as cfg


class DbConnect:
    """Defines methods to connect and disconnect to DB"""

    def __init__(self):
        """Initializes variables and Reads DB Credentials from dbconfig file to config file"""
        logging.info('Reading credentials')
        self.config = {'host': cfg.mysql["host"],
                       'user': cfg.mysql["user"],
                       'password': cfg.mysql["password"],
                       'database': cfg.mysql["database"]
                       }
        logging.info('Credentials read successful')
        self.connection = ''
        self.cursor = ''

    def connect(self):
        """Attempts to connect to DB using credentials from dbconfig file"""
        try:
            logging.info('Trying to connect to SQL')
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            logging.info('Connection Successful')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
            else:
                logging.error(err)

    def disconnect(self):
        """Disconnects to Db"""
        self.connection.commit()
        self.connection.close()
        self.cursor.close()


class DbOperations(DbConnect):
    """Reads Data from Users"""

    def __init__(self, inp):
        """Initializes data"""
        super().__init__()
        super().connect()
        self.userdata = inp

    def insert_into_request_info(self):
        """Inserts data into Request_Info Table"""
        try:
            logging.info('Attempting to insert data into Db')
            sql = "INSERT INTO REQUEST_INFO (FIRST_NAME, MIDDLE_NAME, LAST_NAME,DOB, GENDER," \
                  "NATIONALITY, CURRENT_CITY, STATE, PIN_CODE, QUALIFICATION, SALARY, PAN_NUMBER)"\
                  "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.userdata[0:])
            self.cursor.execute(sql, values)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
            else:
                logging.error(err)

    def insert_into_response_info(self, response):
        """Inserts data into Response_Info Table"""
        try:
            logging.info('Attempting to insert data into Db')
            self.cursor.execute("SELECT ID FROM REQUEST_INFO WHERE PAN_NUMBER = %s",
                                (self.userdata[-1], ))
            request_id = self.cursor.fetchall()
            request_id = request_id[0][0]
            sql = "INSERT INTO RESPONSE_INFO (REQUEST_ID, RESPONSE)"\
                  "VALUES(%s, %s)"
            response = "{'Request_id'" + str(request_id) + response
            values = (request_id, response)
            self.cursor.execute(sql, values)
            logging.info('Closing Connections')
            self.disconnect()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
            else:
                logging.error(err)

    def validate_age(self):
        """Validates Age"""
        gender = self.userdata[4]
        born = self.userdata[3]
        born = datetime.datetime.strptime(born, '%Y-%m-%d')
        today = datetime.date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if gender == 'M' and age > 21:
            return True
        if gender == 'F' and age > 18:
            return True
        return False

    def validate_past_requests(self):
        """This method Checks for past requests"""
        try:
            logging.info("Attempting to read data from DB")
            sql = "SELECT REQUEST_DATE FROM REQUEST_INFO WHERE PAN_NUMBER IN (%s)"
            val = (self.userdata[-1], )
            self.cursor.execute(sql, val)
            db_out = self.cursor.fetchall()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
            else:
                logging.error(err)
        min_age = 6
        today = datetime.date.today()
        if len(db_out) > 1:
            for date in db_out:
                date = date[0]
                age = today.year - date.year - ((today.month, date.day) < (date.month, date.day))
                if age < min_age:
                    min_age = age
            return min_age > 5
        return True

    def validate_nationality(self):
        """Validates Nationality"""
        return self.userdata[5] in ('Indian', 'American')

    def validate_state(self):
        """Validates State"""
        return self.userdata[7] in ('Andhra Pradesh',
                                    'Arunachal Pradesh'
                                    'Assam',
                                    'Bihar',
                                    'Chhattisgarh',
                                    'Karnataka',
                                    'Madhya Pradesh',
                                    'Odisha',
                                    'Tamil Nadu',
                                    'West Bengal')

    def validate_salary(self):
        """Validates Salary"""
        return 10000 <= self.userdata[10] <= 90000

    def validate_data(self):
        """Performs all the validations"""
        response = 'Success'
        reason = 'null'
        if not self.validate_age():
            response = 'Validation Failure'
            reason = 'Age is less than excepted.'
        if not self.validate_past_requests():
            response = 'Validation Failure'
            reason = 'Recently request received in last 5 days.'
        if not self.validate_nationality():
            response = 'Validation Failure'
            reason = 'Nationality should be Indian or American.'
        if not self.validate_state():
            response = 'Validation Failure'
            reason = 'State not matched.'
        if not self.validate_salary():
            response = 'Validation Failure'
            reason = 'Salary is not in Range'
        return reason, response


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
            while inp not in ('M', 'F'):
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
    logging.basicConfig(filename='sql_operations.log',
                        filemode='w',
                        format='%(asctime)s %(levelname)s %(lineno)d - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
                        )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    print("Please provide the following details, fields marked as * are mandatory")
    # 1- Str, 2- int, 3- Date, 4- M/F, 5- not mandatory
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
    dbobj = DbOperations(data)
    dbobj.insert_into_request_info()
    remarks, result = dbobj.validate_data()
    if remarks == 'null':
        OUT_TO_JSON = ", 'Response':}"
        OUT_TO_JSON = OUT_TO_JSON[:13] + result + OUT_TO_JSON[13:]
    else:
        OUT_TO_JSON = ", 'Response':, 'Reason':"
        OUT_TO_JSON = OUT_TO_JSON[:13] + result + OUT_TO_JSON[13:] + result + '}'
    dbobj.insert_into_response_info(OUT_TO_JSON)
    logging.info('Complete')
