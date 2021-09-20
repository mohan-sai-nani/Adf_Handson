"""Adding tables to Admin Page"""
from django.contrib import admin
from .models import RequestInfo, ResponseInfo


admin.site.register(RequestInfo)
admin.site.register(ResponseInfo)
# Register your models here.
