from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
# Create your views here.

from .models import Criminal, crime, Victim


def index(request):
    crim_list = Criminal.objects.all()
    return render(request, 'Templates/display.html', {'crim_list':crim_list})


def caseinfo(request):
    case= get_object_or_404(crime, crime.criminal==Criminal.pk)
    return render(request,'Templates/display1.html',case)