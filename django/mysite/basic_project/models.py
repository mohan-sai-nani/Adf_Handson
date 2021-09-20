"""Defining Table"""
from django.db import models

# Create your models here.


class RequestInfo(models.Model):
    """Table RequestInfo"""
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    nationality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField()
    qualification = models.CharField(max_length=50)
    salary = models.IntegerField()
    pan_number = models.CharField(max_length=50)
    request_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Table name in DB"""
        db_table = 'RequestInfo'


class ResponseInfo(models.Model):
    """Table Response Info"""
    request_id = models.IntegerField(default=None)
    response = models.CharField(max_length=500)

    class Meta:
        """Table name in DB"""
        db_table = 'ResponseInfo'
