from django.shortcuts import render

import requests

from suelo.soil_water_characteristic import wsc
from django.http import HttpResponse

def index(request):

    

    return render(request, 'index.html', {})

def res(request):
    
    return HttpResponse(wsc( S=0.7 , C=0.21 , OM=2.5 ,DF= 1 ,RW=0,CE=5.4 ))
