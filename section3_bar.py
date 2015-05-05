import numpy as np
import pandas
import scipy as sp
from ggplot import *


df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_weather_v2.csv')
countName = 'ENTRIESn_hourly'
differName = 'hour'
differNames = pandas.unique(df[differName])

columns = ['mean','rain','hour']
finalVar = pandas.DataFrame(columns=columns)

i = 0
for var in differNames:

	notRainy = df[df[differName]==var][df['rain']==0]
	rainy = df[df[differName]==var][df['rain']==1]
	
	dfObRain = {}
	# dfObRain['index'] = i
	dfObRain['mean'] = np.mean(rainy[countName])
	dfObRain['rain'] = True
	dfObRain['hour'] = var
	i+=1

	dfObNotRain = {}
	# dfObNotRain['index'] = i
	dfObNotRain['mean'] = np.mean(notRainy[countName])
	dfObNotRain['rain'] = False
	dfObNotRain['hour'] = var
	i+=1

	dfVarRain = pandas.Series(dfObRain)
	finalVar = finalVar.append(dfVarRain,ignore_index=True)

	dfVarNotRain = pandas.Series(dfObNotRain)
	finalVar = finalVar.append(dfVarNotRain,ignore_index=True)


plot1 = ggplot(finalVar,aes(x='hour',y='mean',color='rain')) + geom_line()
print(finalVar)
# plot1 = ggplot(finalVar, aes(x='hour', y='mean')) + geom_bar(position="dodge")

# ggplot(finalVar, aes('latitude','longitude')) \
# + ggtitle('Subways riders on non-rainy days') \
# + labs("ENTRIESn_hourly", "Frequency") \
# + geom_point(aes(colour=factor('meanDif'))) + scale_colour_gradient(limits=[minMean,maxMean], low="red")
print(plot1)