"""Contains all views of basic_project"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import RequestInfo, ReponseInfo
from .validation import UserDataInput
# Create your views here.


def home(request):
    """Renders home page"""
    return render(request, 'home.html')


def validate(request):
    """Reads feedback data"""
    userdata = []
    userdata.append(request.POST['firstname'])
    userdata.append(request.POST['middlename'])
    userdata.append(request.POST['lastname'])
    userdata.append(request.POST['dob'])
    userdata.append(request.POST['gender'])
    userdata.append(request.POST['nationality'])
    userdata.append(request.POST['city'])
    userdata.append(request.POST['state'])
    userdata.append(request.POST['pincode'])
    userdata.append(request.POST['qualification'])
    userdata.append(request.POST['salary'])
    userdata.append(request.POST['pan'])
    req = RequestInfo(first_name=userdata[0],
                      middle_name=userdata[1],
                      last_name=userdata[2],
                      dob=userdata[3],
                      gender=userdata[4],
                      nationality=userdata[5],
                      city=userdata[6],
                      state=userdata[7],
                      pin=userdata[8],
                      qualification=userdata[9],
                      salary=userdata[10],
                      pan_number=userdata[11]
                      )
    req.save()
    validatation_obj = UserDataInput(userdata)
    remarks, result = validatation_obj.validate_data()
    if remarks == 'null':
        json_response = ", 'Response':}"
        json_response = json_response[:13] + result + json_response[13:]
    else:
        json_response = ", 'Response':, 'Reason':"
        json_response = json_response[:13] + result + json_response[13:] + remarks + '}'
    req_id = RequestInfo.objects.latest('id').id
    res = ReponseInfo(request_id=req_id, response=json_response)
    res.save()
    return HttpResponse("Thank You")
