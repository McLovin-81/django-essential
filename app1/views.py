from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

# Create your views here.

# REQUEST -> RESPONSE or REQUEST HANDLER

def showDate(request):
    return render(request, "app1/welcome.html", {"today": datetime.today()})