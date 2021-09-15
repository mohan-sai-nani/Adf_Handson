from django.db import models

# Create your models here.


class RequestInfo(models.Model):
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


class ReponseInfo(models.Model):
    request_id = models.ForeignKey(RequestInfo, on_delete=models.CASCADE)
    response = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)