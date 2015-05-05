import numpy as np
import pandas
import r_squared
import scipy as sp
from ggplot import *


df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_weather_v2.csv')
stationNames = pandas.unique(df['station'])
countName = 'ENTRIESn_hourly'
stationName = 'station'
colNames =[stationName,countName,'longitude','latitude']

rainy = df[df.rain == 1][colNames]
notRainy = df[df.rain == 0][colNames]

columns = ['index','meanDif','latitude','longitude','station']
finalVar = pandas.DataFrame(columns=columns)
f = open('/Users/aha/Documents/workspace/udacity/p1/furtherAnalysis.txt', 'w')

i = 0
for var in stationNames:
	notRainyStation = notRainy[notRainy.station==var]
	rainyStation = rainy[rainy.station==var]

	notRainyAr=notRainyStation[countName]
	rainyAr=rainyStation[countName]
	
	meanRainy =  np.mean(rainyAr)
	meanNotRainy =  np.mean(notRainyAr)
	meanDif = meanRainy - meanNotRainy
	latitude = notRainyStation['latitude'].head(1)
	longitude = notRainyStation['longitude'].head(1)

	dfOb = {}
	dfOb['index'] = i
	dfOb['meanDif'] = 0
	dfOb['latitude'] = latitude
	dfOb['longitude'] = longitude
	dfOb['station'] = var
	dfOb['meanDif'] = meanDif
	
	i=+1

	U,p ="",""
	if len(notRainyAr) > 20 and len(rainyAr) > 20 and len(set(notRainyAr)) >1 and len(set(rainyAr))>1:
		U,p =sp.stats.mannwhitneyu(rainyAr,notRainyAr)
		# finalVar[var] = (str(U) + " " + str(p) + ' rainMean: '+ str(meanRainy) +' meanNotRainy: '+ str(meanNotRainy))
		# f.write(var +" "+finalVar[var]+ '\n')
		if p < 0.05:
			print(var + " " + str(p)) 
	else:
		print(var + "\n")
		dfOut = df[df.station == var]
		# dfOut.to_csv('/Users/aha/Documents/workspace/udacity/p1/'+var+'Excluded.csv')

	dfVar = pandas.DataFrame(dfOb)
	finalVar = finalVar.append(dfVar)
# print(finalVar)
#pandas.DataFrame(stationNames)
minMean = finalVar['meanDif'].min()
maxMean = finalVar['meanDif'].max()
# col = []
# for var in stationNames:
# 	temp = finalVar[finalVar.station==var]
# 	col.append(rgb(minMean,maxMean,temp['meanDif']))

# finalVar['rgb'] = Series(col, index=finalVar.index)
# print(col)
# print(finalVar)

plot1 = ggplot(aes(x='latitude', y='longitude', colour='meanDif'), data=finalVar) + \
    geom_point() + scale_colour_gradient(low = "red", high="green")

# ggplot(finalVar, aes('latitude','longitude')) \
# + ggtitle('Subways riders on non-rainy days') \
# + labs("ENTRIESn_hourly", "Frequency") \
# + geom_point(aes(colour=factor('meanDif'))) + scale_colour_gradient(limits=[minMean,maxMean], low="red")
print(plot1)





