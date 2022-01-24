from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import pandas as pd
from .algorithms import algorithms as alg
from .algorithms import table as tb 
import numpy as np
from django.http import FileResponse
from matplotlib import rcParams
from .pyRadialPlot import general_radial
import time

rcParams["figure.dpi"] = 300

# Create your views here.
def index( request):
    return render(request, 'index.html')

@csrf_exempt
def calzeta( request):
    #print(request.body)
    req = json.loads( request.body )
    table = req['mytable']
    [head, data] = tb.rqbody2frame(table)
    adata={}
    fmt = int( req['method'] )
    err = int( req['input_errors'] )
    if fmt == 1:
        adata['data']= data
        adata['zeta']= float( req['zetaVal'] )
        adata['zetaErr'] = float( req['zetaErr'] )
        adata['rhoD']= float( req['rhoDval'] )
        adata['rhoDerr']= float( req['rhoDerr'] )
       
    elif fmt == 2:
        adata['data']= data
        adata['zeta']= float( req['standAgeVal'] )
        adata['zetaErr'] = float( req['standAgeErr'] )
        adata['spotSize']= float( req['spot_size'])

    elif fmt == 3:
        adata['data']= data
        adata['mineral']= req['mineral'] 
        adata['spotSize']= float( req['spot_size'])	
    adat = alg.selection2data(adata, method='fissiontracks',formt=fmt,ierr=err)
    tao = alg.setZeta(adat,tst=[100,1.0],exterr=False,sigdig=2,update=False)
    return JsonResponse( {'mydata':{0:tao}} )

@csrf_exempt
def calages( request):
    req = json.loads( request.body )
    table = req['mytable']
    
    [head, data] = tb.rqbody2frame(table)
    adata={}
    fmt = int( req['method'] )
    err = int( req['input_errors'] )
    data = data.reset_index(drop=True)
    data = data.replace(to_replace=[None], value=np.nan)
    if fmt == 1:
        adata['data']= data
        adata['zeta']= float( req['zetaVal'] )
        adata['zetaErr'] = float( req['zetaErr'] )
        adata['rhoD']= float( req['rhoDval'] )
        adata['rhoDerr']= float( req['rhoDerr'] )
    elif fmt == 2:
        adata['data']= data
        adata['zeta']= float( req['M_zetaVal'] )
        adata['zetaErr'] = float( req['M_zetaErr'] )
        adata['spotSize']= float( req['spot_size'])
    elif fmt == 3:
        adata['data']= data
        adata['mineral']= req['mineral'] 
        adata['spotSize']= float( req['spot_size'])	
        
    adat = alg.selection2data(adata, method='fissiontracks',formt=fmt,ierr=err)
    ts = alg.ageFissionTracks(adat,exterr=False,sigdig=2)
    tsdict = tb.frame2json(ts)
    return JsonResponse( {'mydata':tsdict} )

@csrf_exempt
def image(request):
	req = json.loads( request.body )
	table = req['mytable']
	[head, data] = tb.rqbody2frame(table)

	adata={}
	fmt = int( req['method'] )
	err = int( req['input_errors'] )
	data = data.reset_index(drop=True)
	data = data.replace(to_replace=[None], value=np.nan)
	if fmt == 1:
		adata['data']= data
		adata['zeta']= float( req['zetaVal'] )
		adata['zetaErr'] = float( req['zetaErr'] )
		adata['rhoD']= float( req['rhoDval'] )
		adata['rhoDerr']= float( req['rhoDerr'] )
	elif fmt == 2:
		adata['data']= data
		adata['zeta']= float( req['M_zetaVal'] )
		adata['zetaErr'] = float( req['M_zetaErr'] )
		adata['spotSize']= float( req['spot_size'])
	elif fmt == 3:
		adata['data']= data
		adata['mineral']= req['mineral'] 
		adata['spotSize']= float( req['spot_size'])	
        
	adat = alg.selection2data(adata, method='fissiontracks',formt=fmt,ierr=err)
	ts = alg.ageFissionTracks(adat,exterr=False,sigdig=2)
    
	general_radial(estimates=ts['t'], standard_errors=ts['s[t]'], transform="logarithmic")
	time.sleep(1)

	img = open(r'C:\Users\lly\Desktop\now\fissionTracks\fissionTracks\calculation\static\img\general.png', 'rb')
	response = FileResponse(img)
	return response