from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.

from .models import Criminal, crime, Victim


def index(request):
    crim_list = Criminal.objects.all()
    return render(request, 'Templates/display.html', {'crim_list':crim_list})


def caseinfo(request, cid):
    cc = Criminal.objects.get(id=cid)
    case = cc.crime.all()
    #case= crime.objects.filter(criminal.id==cid)
    #return HttpResponse(cid)
    return render(request,'Templates/display1.html',{'case': case})
