from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import os

import pandas as pd
# from algorithm.calGeothermal import Geothermal


# Create your views here.
def index( request):
    return render(request, 'index.html')

@csrf_exempt
def caltao( request):
	req = json.loads( request.body )
	print(req)
	# geo = Geothermal( os.getcwd()+'\\mymap\\data\\')

	# selPos = req['selPos']
	# depth = req['depth']
	# result = geo.caltmprt( float(depth) )
	tmp = {'tao': str(round(1.25, 1)) }
	#print(tmp)
	return JsonResponse( tmp )



