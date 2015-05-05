import numpy as np
import scipy as sp
import pandas
from pandas import DataFrame, Series
from ggplot import *
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_weather_v2.csv')

countName = 'ENTRIESn_hourly'
differName = 'hour'
differNames = pandas.unique(df[differName])

colNames =[differName,countName]

rainy = df[df.rain == 1][colNames]
notRainy = df[df.rain == 0][colNames]

finalVar = {}
f = open('/Users/aha/Documents/workspace/udacity/p1/furtherAnalysis.txt', 'w')
fSig = open('/Users/aha/Documents/workspace/udacity/p1/furtherAnalysis_fSig.txt', 'w')
for var in differNames:
	
	notRainyAr=notRainy[notRainy[differName]==var][countName]
	rainyAr=rainy[rainy[differName]==var][countName]
	meanRainy =  np.mean(rainyAr)
	meanNotRainy =  np.mean(notRainyAr)
	U,p ="",""
	if len(notRainyAr) > 20 and len(rainyAr) > 20 and len(set(notRainyAr))>1and len(set(rainyAr))>1:
		U,p =sp.stats.mannwhitneyu(rainyAr,notRainyAr)
		finalVar[var] = (str(U) + " " + str(p) + ' rainMean: '+ str(meanRainy) +' meanNotRainy: '+ str(meanNotRainy))
		f.write(str(var) +" "+finalVar[var]+ '\n')
		if p < 0.05:
			fSig.write(str(var) +" "+finalVar[var]+ '\n')
			print(str(var) + " " + str(p)) 
	else:
		print(str(var) + "\n")
		dfOut = df[df[differName] == var]
		# dfOut.to_csv('/Users/aha/Documents/workspace/udacity/p1/'+var+'Excluded.csv')

# print(finalVar)
#pandas.DataFrame(stationNames)
