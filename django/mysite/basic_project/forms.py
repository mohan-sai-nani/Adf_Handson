"""From to get data from User"""
from django import forms
from .models import RequestInfo


class RequestForm(forms.ModelForm):
    """Add data to RequestInfo"""
    class Meta:
        """Make a from to collect data"""
        model = RequestInfo
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'dob',
            'gender',
            'nationality',
            'city',
            'state',
            'pin',
            'qualification',
            'salary',
            'pan_number'
        ]
