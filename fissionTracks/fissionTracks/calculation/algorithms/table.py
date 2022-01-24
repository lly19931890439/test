import pandas as pd
import numpy as np

def rqbody2frame(table):
	tmplst=[]
	for i in table.keys():
	    b= table[i]
	    # print(b)
	#     print(b.values())
	    c= b.values()
	    # print(c)
	    d= [j['value'] for j in c]
	    # print(d)
	    tmplst.append(d)

	head= tmplst[0]
	# print(tmplst)

	data= pd.DataFrame(columns=head )
	for i in range(len(tmplst)):
		if i==0:
			continue
		arow = tmplst[i]
		arow = [float(j) for j in arow]
		#print(arow)
		# arow= table[i].valu
		# arow= [j['values']]
		# if len(arow) != len(head):
		for j in range(len(head)-len(arow)):
			arow.append(None)
		#print(arow)
		tmpdata = pd.DataFrame([arow], columns=head)

		data = data.append( tmpdata )
	data = data.reset_index(drop=True)
	data = data.replace(to_replace=[None], value=np.nan)

	return head, data 

def frame2json(ts):
	tsdict = {}
	head = ts.columns 
	for index, row in ts.iterrows():
		tmpdic = {}
		for i in head:
			tmpdic[i] = row[i]
		tsdict[index] = tmpdic
	# print(tsdict)
	return tsdict