"""Contains all views of basic_project"""
from django.shortcuts import render
from .models import RequestInfo
from django.http import HttpResponse
# Create your views here.


def home(request):
    """Renders home page"""
    return render(request, 'home.html')


def validate(request):
    """Reads feedback data"""
    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    lastname = request.POST['lastname']
    dob = request.POST['dob']
    gender = request.POST['gender']
    nationality = request.POST['nationality']
    city = request.POST['city']
    state = request.POST['state']
    pincode = request.POST['pincode']
    qualification = request.POST['qualification']
    salary = request.POST['salary']
    pan = request.POST['pan']
    dbobj = RequestInfo(first_name=firstname, middle_name=middlename, last_name=lastname, dob=dob,
                        gender=gender, nationality=nationality, city=city, state=state, pin=pincode,
                        qualification=qualification, salary=salary, pan_number=pan)
    dbobj.save()
    return HttpResponse("Thank You")
