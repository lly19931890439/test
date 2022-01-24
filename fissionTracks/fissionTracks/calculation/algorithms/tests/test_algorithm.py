import sys
import os
  
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

import algorithms as alg


import pandas as pd

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('../../ressources/datafission_age_f1_e1.csv')
# data['zeta']=100
# data['zetaErr'] = 10
# data['rhoD']=1000000
# data['rhoDerr']=5000
# dat = alg.selection2data(data, method='fissiontracks',formt=1,ierr=1)
# print( alg.ageFissionTracks(dat,exterr=False,sigdig=2) )
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('../../ressources/datafission_age_f2_e1_1.csv')
# data['zeta']= 3000
# data['zetaErr'] = 20
# data['spotSize']= 20
# dat = alg.selection2data(data, method='fissiontracks',formt=2,ierr=1)
# print(dat)
# print( alg.ageFissionTracks(dat,exterr=False,sigdig=2) )

# data={}
# data['nr']=100
# data['nc']=14
# data['data']=pd.read_csv('../../ressources/datafission_age_f3_e1_1.csv')
# data['mineral'] = 'apatite'
# data['spotSize']= 20
# dat = alg.selection2data(data, method='fissiontracks',formt=3,ierr=1)
# print( alg.ageFissionTracks(dat,exterr=False,sigdig=2) )
# setZeta(dat,tst=[100,1.0],exterr=False,sigdig=2,update=False)



# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('../../ressources/datafission_age_f1_e1.csv')
# data['zeta']=350
# data['zetaErr'] = 10
# tval = 20
# terr = 1
# data['rhoD']=1000000
# data['rhoDerr']=10000
# dat = alg.selection2data(data, method='fissiontracks',formt=1,ierr=1)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# print( alg.setZeta(dat,tst=[tval,terr],exterr=False,sigdig=2,update=False) )

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('../../ressources/datafission_age_f2_e1_1.csv')
# data['zeta']=350
# data['zetaErr'] = 10
# tval = 50
# terr = 1
# data['rhoD']=1000000
# data['rhoDerr']=10000
# data['spotSize']= 20
# dat = alg.selection2data(data, method='fissiontracks',formt=2,ierr=1)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# print( alg.setZeta(dat,tst=[tval,terr],exterr=False,sigdig=2,update=False) )

# data={}
# data['nr']=100
# data['nc']=4
# data['data']=pd.read_csv('../../ressources/datafission_age_f3_e1_1.csv')
# data['zeta']=350
# data['zetaErr'] = 10
# tval = 50
# terr = 1
# data['rhoD']=1000000
# data['rhoDerr']=10000
# data['spotSize']= 20
# data['mineral'] = 'apatite'
# dat = alg.selection2data(data, method='fissiontracks',formt=3,ierr=1)
# # ageFissionTracks(dat,exterr=False,sigdig=2)
# print( alg.setZeta(dat,tst=[tval,terr],exterr=False,sigdig=2,update=False) )