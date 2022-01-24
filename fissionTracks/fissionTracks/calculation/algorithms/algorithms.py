#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import sys
import math
import copy


# In[3]:



def errAdjust(x, i=1, ierr=1):
    out = copy.deepcopy(x)
    if type(x) == list:
        if ierr==2:
            out[i] = x[i]/2
        elif ierr ==3:
            out[i] = x[i]*x[i-1]/100
        elif ierr ==4:
            out[i] = x[i]*x[i-1]/200
    else:
        if ierr==2:
            out.iloc[:,i] = x.iloc[:,i]/2
        elif ierr==3:
            ic = [tmp-1 for tmp in i]
            name = [str(i) for i in range(len(i))]
            mtx1 = x.iloc[:,i]
            mtx1.set_axis(name, axis=1, inplace=True)
            mtx2 = x.iloc[:,ic]
            mtx2.set_axis(name, axis=1, inplace=True)
            out.iloc[:,i] = mtx1*mtx2/100
        elif ierr==4:
            ic = [tmp-1 for tmp in i]
            name = [str(i) for i in range(len(i))]
            mtx1 = x.iloc[:,i]
            mtx1.set_axis(name, axis=1, inplace=True)
            mtx2 = x.iloc[:,ic]
            mtx2.set_axis(name, axis=1, inplace=True)
            out.iloc[:,i] = mtx1*mtx2/200
    return out

def selection2data(inpt,method="U-Pb",formt=1,ierr=1,Th02=(0,0),Th02U48=(0,0,1e6,0,0,0,0,0,0), ):
    out = {}
    out['format'] = formt
    nc = inpt['data'].shape[1]
    if formt == 1:
        out['zeta'] = errAdjust([inpt['zeta'], inpt['zetaErr']] , ierr=ierr )
        out['rhoD'] = errAdjust([inpt['rhoD'], inpt['rhoDerr']] , ierr=ierr )
        out['x'] = inpt['data']
        return out
    else:
        if formt==2:
            out['zeta'] = errAdjust([inpt['zeta'], inpt['zetaErr']] , ierr=ierr )
        else:
            out['mineral'] = inpt['mineral']
        out['spotSize']= inpt['spotSize']
        out['Ns'] = inpt['data']['Ns']
        out['A'] = inpt['data']['A']
        
        iU=[i for i in range(2, nc-1, 2)]
        isU=[i for i in range(3, nc, 2 )]
        UsU = errAdjust( copy.deepcopy(inpt['data']), isU, ierr=ierr)
        
        out['U'] = UsU.iloc[:, iU[0:-1] ]
        out['sU'] = UsU.iloc[:, isU[0:-1]]
    return out


# In[4]:


constants={ 
  "lambda": {
	"fission": [8.5e-11,0.1e-11],
	"U238":  [0.000155125,0.000000083],
	"U235":  [0.00098485,0.00000067],
	"U234":  [0.00282206,0.00000080],
	"Th232": [0.0000495,0.0000025],
	"Th230": [0.0091705,0.0000016],
	"Pa231": [0.021158,0.00071],
	"Ra226": [0.4332,0.0019],
	"Rb87":  [0.000013972,0.000000450],
	"Re187": [0.00001666,0.000000085],
	"Sm147": [0.000006524,0.000000012],
	"K40":   [0.00055305,0.00000132],
	"Lu176": [0.00001867,0.00000008]
    },
    "iratio": {
	"Ar40Ar36": [298.56,0.31],
	"Ar38Ar36": [0.1885,0.0003],
	"Ca40Ca44": [46.480,0.044],
	"Rb85Rb87": [2.59265,0.00085],
	"Sr84Sr86": [0.056549,0.0000715],
	"Sr87Sr86": [0.69938,0.00006],
	"Sr88Sr86": [8.37861,0.001624],
	"Re185Re187": [0.59738,0.000195],
	"Os184Os192": [0.000485,0.00011],
	"Os186Os192": [0.03889,0.00011],
	"Os187Os192": [0.04817,0.00003],
	"Os188Os192": [0.32474,0.00005],
	"Os189Os192": [0.39593,0.00004],
	"Os190Os192": [0.64388,0.00045],
	"Th230Th232": [0,0],
	"U234U238": [0,0],
	"U238U235": [137.818,0.0225],
	"Pb206Pb204": [9.307,0],
	"Pb207Pb204": [10.294,0],
	"Pb207Pb206": [1.1060,0],
	"Pb208Pb204": [29.476,0],
	"Pb208Pb206": [3.1671,0],
	"Pb208Pb207": [2.8634,0],
	"Sm144Sm152": [0.115117,0.000189],
	"Sm147Sm152": [0.561134,0.000622],
	"Sm148Sm152": [0.420634,0.000392],
	"Sm149Sm152": [0.516973,0.000393],
	"Sm150Sm152": [0.275438,0.000459],
	"Sm154Sm152": [0.850468,0.000484],
	"Nd142Nd144": [1.14101,0.00070],
	"Nd143Nd144": [0.51154,0.00040],
	"Nd145Nd144": [0.34848,0.00015],
	"Nd146Nd144": [0.72228,0.00051],
	"Nd148Nd144": [0.24186,0.00030],
	"Nd150Nd144": [0.23691,0.00042],
	"Lu176Lu175": [0.026680,0.000013],
	"Hf174Hf177": [0.00871,0.00005],
	"Hf176Hf177": [0.2829,0.0030],
	"Hf178Hf177": [1.46710,0.00010],
	"Hf179Hf177": [0.7325,0],
	"Hf180Hf177": [1.88651,0.00012]	
    },
    "imass": {
	"U":    [238.02891,0.00003],
	"Rb":   [85.46776,0.00026],
	"Rb85": [84.9117924,0.0000027],
	"Rb87": [86.9091828,0.0000028],
	"Sr":   [87.62,0.01],
	"Sr84": [83.913426,0.000004],
	"Sr86": [85.9092647,0.0000025],
	"Sr87": [86.9088816,0.0000025],
	"Sr88": [87.9056167,0.0000025],
	"Re":   [186.20679,0.00031],
	"Re185": [184.952955,0.000003],
	"Re187": [186.9557505,0.0000030],
	"Os":    [190.23,0.003],
	"Os184": [183.952491,0.000003],
	"Os186": [185.953838,0.000003],
	"Os187": [186.9557476,0.0000030],
	"Os188": [187.9558357,0.0000030],
	"Os189": [188.958145,0.000003],
	"Os190": [189.958445,0.000003],
	"Os192": [191.961479,0.000004],
	"Sm": [150.36,0.03],
	"Nd": [144.2415,0.0013],
	"Lu": [174.9668,0.0001],
	"Hf": [178.49,0.02]
    },
    "etchfact": {
	"apatite": 0.93,
	"zircon": 1
    },
    "tracklength": {
	"apatite": 16.2,
	"zircon": 10.6
    },
    "mindens": {
	"apatite": 3.22,
	"zircon": 4.7
    }
}


# In[5]:


myNs=''
def getEDMAge(Ns,Ni,zeta,rhoD=[1,0]):
    L8 = constants['lambda']['U238'][0]
    if (Ns<1):
        Ns = Ns+0.5
        Ni = Ni+0.5
    tt = math.log(1+0.5*L8*(zeta[0]/1e6)*rhoD[0]*(Ns/Ni))/L8
    st = tt*math.sqrt(1/Ns + 1/Ni + (rhoD[1]/rhoD[0])**2 + (zeta[1]/zeta[0])**2)
    return [tt,st]

def getICPAge(Ns,A,UsU,zeta):
    # print('111111111111112222222222222222')
    # print(Ns)
    # print('-------------')
    # print(A)
    # print('-------------')
    # print(UsU)
    # print('-------------')
    # print(zeta)
    # print('-----------')
    # print(UsU[0])
    # print('--------')
    # print(UsU.values)
    # print('4444444444444444444444444444444')
    L8 = constants['lambda']['U238'][0]
    tt = math.log(1+L8*zeta[0]*Ns/(2*UsU.values[0]*A))/L8
    st = tt * math.sqrt(1/Ns + (zeta[1]/zeta[0])**2 + (UsU.values[1]/UsU.values[0])**2)
    return [tt,st]

def getUsU(x):
    Aicp = math.pi*(x['spotSize']/2)**2
    n = len(x['U'])
    nspots = x['U'].count().sum()
    doAverage = (nspots>n)
    out = pd.DataFrame(columns=['U', 'sU'])

    m = [0 for i in range(n)]
    if (doAverage):
        uhat = [0 for i in range(n)]
        num = 0
        den = 0
    for j in range(n):
        if (doAverage):
            y = x['U'].iloc[j]
            Uj = y[y.notnull()]
            m[j] = len(Uj) # spots per grain
            uhat[j] = np.mean(np.log(Uj))
            num = num + sum((np.log(Uj)-uhat[j])**2)
            den = den + m[j] - 1
        else :
            y = x['U'].iloc[j]
            U  = y[y.notnull()][0]
            y = x['sU'].iloc[j]
            sU = y[y.notnull()][0]
            
            # print('00000000000000')
            # print(U)
            # print(sU)

            to_append = [U,sU]
            a_series = pd.Series(to_append, index = ['U', 'sU'] )
            out = out.append(a_series, ignore_index=True)
    # print('```````````````````````')
    # print(out)
    # print('++++++++++++++++++++++')            
    if (doAverage):
        out['U'] = np.exp(uhat)
        vhat = [num/den for i in range(n)]
        for j in range(n):
            xsU= x['sU'].iloc[j].values
            xU = x['U'].iloc[j].values
            
            suhat = xsU/xU
#             print(vhat[j],'  ', m[j], '  ', Aicp, '  ', x['A'][j], '  ', suhat, '  ')
#             print(np.nansum(suhat**2))
            vhat[j] = vhat[j]*(1-m[j]*Aicp/x['A'][j])**2 + np.nansum(suhat**2) *(Aicp/x['A'][j])**2
#             print(vhat[j])
#             print(suhat**2)
#         print('=========-=====================vhat uhat')
        out['sU'] = np.exp(uhat)*np.sqrt(vhat)
#         print(uhat)
#         print('--------------')
#         print(vhat)
    # print('```````````````````````')
    # print(out)
    # print('++++++++++++++++++++++')
    return out

def ICPAge(x,i=None,sigdig=None,exterr=True):
    ngrains = len(x['Ns'])
    tt = []
    st = []
    if (exterr):
        zeta = x['zeta']
    else:
        zeta = [x['zeta'][0],0]
    ipos = [i for i in range(len(x['Ns'])) if x['Ns'][i]>0 ]
    izero = [i for i in range(len(x['Ns'])) if x['Ns'][i]<1 ]
    UsU = getUsU(x)
    # print('UsU========================UsU')
    # print(UsU)

    # first calculate the ages of the non-zero track data:
#     print('tst==================tst')
    for i in ipos:
        tst = getICPAge(x['Ns'].values[i],x['A'].values[i],UsU.iloc[i] ,zeta)
#         print(tst)
        tt.append( tst[0] )
        st.append( tst[1] )
    # then use the equivalent induced track approach:
    for i in izero:
        rho = UsU['U'][i] /(x['A'][i]*UsU['sU'][i]**2)
        Ni = x['A'][i]*UsU['U'][i]*rho
        tst = getEDMAge(x['Ns'][i],Ni,zeta*1e6,[rho,0] )
#         print(tst)
        tt.append(tst[0]) 
        st.append(tst[1])
    tt = [round(i, sigdig-1) for i in tt]
    st = [round(i, sigdig-1) for i in st]
#     print('============tt st ========')
#     print(tt)
#     print('--------')
#     print(st)
    out = pd.DataFrame()
    out['t'] = tt
    out['s[t]'] = st
    return out

def getAbsoluteZeta(mineral,exterr=False):
    R = constants['iratio']['U238U235'][0]
    MM = constants['imass']['U'][0]
    qap = constants['etchfact'][mineral] 
    L = constants['tracklength'][mineral] 
    Lf = constants['lambda']['fission'][0]
    dens = constants['mindens'][mineral]
    Na = 6.02214e23
    zeta = 4*(1+R)*MM*1e18/(Na*Lf*qap*L*dens*R)
    if (exterr):
        Lf = constants['lambda']['fission']
        szeta = zeta*Lf[1]/Lf[0]
    else:
        szeta = 0
    return [zeta,szeta]

def EDMAge(x,i=None,sigdig=2,exterr=True):
    out = pd.DataFrame(columns=['t', 's[t]'])
    if (exterr):
        zeta = x['zeta']
        rhoD = x['rhoD']
    else:
        zeta = [x['zeta'][0],0]
        rhoD = [x['rhoD'][0],0]
    for index, row in x['x'].iterrows():
#         print(row['Ns'], row['Ni'])
        tt = getEDMAge(row['Ns'], row['Ni'], zeta, rhoD)
        outj= [ round(tt[0], sigdig-1), round(tt[1], sigdig-1)]
        
        a_series = pd.Series(outj, index = ['t', 's[t]'] )
        out = out.append(a_series, ignore_index=True)
        
    if (i!=None):
        out = out.iloc[i]
    return out

def fissionTracksAge(x,i=None,sigdig=None,exterr=True):
    if (x['format'] < 2):
        return EDMAge(x,i,sigdig=sigdig,exterr=exterr)
    elif (x['format']> 1):
        if (x['format'] == 3):
            x['zeta']= getAbsoluteZeta(x['mineral'],exterr=exterr);
        return ICPAge(x,i,sigdig=sigdig,exterr=exterr)

def ageFissionTracks(x, central=False, i=None, sigdig= None, exterr=True ):
    if central :
        return centralFunc(x)
    else:
        return fissionTracksAge(x, i=i, sigdig=sigdig, exterr= exterr )


# In[6]:



# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 10
# data['rhoD']=2500000
# data['rhoDerr']=10000
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=1)
# # ageFissionTracks(dat,exterr=True,sigdig=2)
# dat


# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 20
# data['rhoD']=2500000
# data['rhoDerr']=20000
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=2)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 2.9
# data['rhoD']=2500000
# data['rhoDerr']=0.4
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=3)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 5.8
# data['rhoD']=2500000
# data['rhoDerr']=0.8
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=4)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f2_e1.csv')
# data['zeta']=9700
# data['zetaErr'] = 49
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=2,ierr=1)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f2_e2.csv')
# data['zeta']=9700
# data['zetaErr'] = 100
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=2,ierr=2)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f2_e3.csv')
# data['zeta']=9700
# data['zetaErr'] = 0.515
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=2,ierr=3)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e1.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=3,ierr=1)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e2.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=3,ierr=2)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e3.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=3,ierr=3)
# ageFissionTracks(dat,exterr=False,sigdig=2)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e4.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat=selection2data(data, method='fissiontracks',formt=3,ierr=4)
# ageFissionTracks(dat,exterr=True,sigdig=2)


# In[ ]:





# In[ ]:





# In[7]:


# get tao
# set zeta


# In[8]:


def setZeta(x,tst,exterr=True,update=True,sigdig=2):
#     N = len(x['Ns'])
    L8 = constants['lambda']['U238'][0]
    tt = tst[0]
    if (exterr) :
        st = tst[1]
    else :
        st = 0
    if (x['format']==1):
        Ns = sum(x['x']['Ns'])
        Ni = sum(x['x']['Ni'])
        rhoD = x['rhoD']
        if (not exterr):
            rhoD[1] = 0
        zeta = 2e6*(np.exp(L8*tt)-1)/(L8*rhoD[0]*Ns/Ni)
        zetaErr = zeta * np.sqrt( (L8*np.exp(L8*tt)*st/(np.exp(L8*tt)-1))**2 + (rhoD[1]/rhoD[0])**2 + 1/Ns + 1/Ni )
    else:
        Ns = sum(x['Ns'] )
        UsU = getUsU(x)
        UA = sum(UsU['U']*x['A'])
        UAerr = np.sqrt( sum(UsU['sU']*x['A'])**2 )
        zeta = 2*UA*(np.exp(L8*tt)-1)/(L8*Ns)
        zetaErr = zeta * np.sqrt( ((L8*np.exp(L8*tt)*st)/(np.exp(L8*tt)-1))**2 + 1/Ns + (UAerr/UA)**2 )
#     zsz = roundit(zeta,zetaErr,sigdig=sigdig)
    out = {}
    zsz= [round(zeta, sigdig-1), round( zetaErr, sigdig-1)]
    if (update):
        out = x
        out['zeta'] = zsz
    else :
        out['zeta'] =  zsz[0]
        out['s[zeta]']= zsz[1]

    return out


# In[9]:



# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 10
# data['rhoD']=2500000
# data['rhoDerr']=10000
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=1)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)


# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 20
# data['rhoD']=2500000
# data['rhoDerr']=20000
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=2)
# ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 2.9
# data['rhoD']=2500000
# data['rhoDerr']=0.4
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=3)
# ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 5.8
# data['rhoD']=2500000
# data['rhoDerr']=0.8
# dat = selection2data(data, method='fissiontracks',formt=1,ierr=4)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('datafission_gettao_f2_e1.csv')
# data['zeta']=9700
# data['zetaErr'] = 49
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=2,ierr=1)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f2_e2.csv')
# data['zeta']=9700
# data['zetaErr'] = 100
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=2,ierr=2)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f2_e3.csv')
# data['zeta']=9700
# data['zetaErr'] = 0.515
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=2,ierr=3)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e1.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=3,ierr=1)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e2.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=3,ierr=2)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e3.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat = selection2data(data, method='fissiontracks',formt=3,ierr=3)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('datafission_age_f3_e1.csv')
# data['zeta']=9700
# data['zetaErr'] = 0.515
# data['mineral'] = 'apatite'
# data['spotSize']= 35
# dat=selection2data(data, method='fissiontracks',formt=3,ierr=4)
# dat
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)


# In[ ]:




