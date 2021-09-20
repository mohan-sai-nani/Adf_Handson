"""Validates user Input"""
import datetime


class UserDataInput:
    """userdata getting initialized in the constructor"""
    def __init__(self, userdata):
        self.userdata = userdata

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
        return 10000 <= int(self.userdata[10]) <= 90000

    def validate_data(self):
        """Performs all the validations"""
        response = 'Success'
        reason = ''
        if not self.validate_age():
            response = 'Validation Failure'
            reason += 'Age is less than expected.'
        if not self.validate_nationality():
            response = 'Validation Failure'
            reason += 'Nationality should be Indian or American.'
        if not self.validate_state():
            response = 'Validation Failure'
            reason += 'State not matched.'
        if not self.validate_salary():
            response = 'Validation Failure'
            reason += 'Salary is not in Range'
        return reason, response
