"""Contains all views of basic_project"""
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import RequestInfo, ResponseInfo
from .validation import UserDataInput
from .forms import RequestForm
# Create your views here.


class Validate(View):
    """Handles get and Post requests"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.userdata = []

    def get(self, request):
        """Renders home page"""
        return render(request, 'home.html')

    def post(self, request):
        """Reads feedback data"""
        self.userdata.append(request.POST['firstname'])
        self.userdata.append(request.POST['middlename'])
        self.userdata.append(request.POST['lastname'])
        self.userdata.append(request.POST['dob'])
        self.userdata.append(request.POST['gender'])
        self.userdata.append(request.POST['nationality'])
        self.userdata.append(request.POST['city'])
        self.userdata.append(request.POST['state'])
        self.userdata.append(request.POST['pincode'])
        self.userdata.append(request.POST['qualification'])
        self.userdata.append(request.POST['salary'])
        self.userdata.append(request.POST['pan'])
        req = RequestInfo(first_name=self.userdata[0],
                          middle_name=self.userdata[1],
                          last_name=self.userdata[2],
                          dob=self.userdata[3],
                          gender=self.userdata[4],
                          nationality=self.userdata[5],
                          city=self.userdata[6],
                          state=self.userdata[7],
                          pin=self.userdata[8],
                          qualification=self.userdata[9],
                          salary=self.userdata[10],
                          pan_number=self.userdata[11]
                          )
        req.save()
        validatation_obj = UserDataInput(self.userdata)
        remarks, result = validatation_obj.validate_data()
        if remarks == '':
            json_response = ", 'Response':}"
            json_response = json_response[:13] + result + json_response[13:]
        else:
            json_response = ", 'Response':, 'Reason':"
            json_response = json_response[:13] + result + json_response[13:] + remarks + '}'
        req_id = RequestInfo.objects.latest('id').id
        res = ResponseInfo(request_id=req_id, response=json_response)
        res.save()
        return HttpResponse(json_response)


def Requestform(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RequestForm()
    context = {
        'form': form
    }
    return render(request, "Request_form.html", context)
