import numpy as np
import pandas
import scipy as sp
from ggplot import *


df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_weather_v2.csv')
countName = 'EXITSn_hourly'
differName = 'hour'
differNames = pandas.unique(df[differName])

columns = ['mean','rain','hour']
finalVar = pandas.DataFrame(columns=columns)

i = 0
for var in differNames:
   notRainy = df[(df[differName]==var) & (df['rain']==False)]
   # rainy = df[df[differName]==var][df['rain']==True]

   # dfObRain = {}
   # dfObRain['mean'] = np.mean(rainy[countName])
   # dfObRain['rain'] = "rain"
   # dfObRain['hour'] = var
   
   # # finalVar.loc[i] = [np.mean(rainy[countName]),"rain",var]
   # i+=1

   # dfObNotRain = {}
   # dfObNotRain['mean'] = np.mean(notRainy[countName])
   # dfObNotRain['rain'] = "no rain"
   # dfObNotRain['hour'] = var
   # # finalVar.loc[i] = [np.mean(notRainy[countName]),"norain",var]
   # i+=1

# plot = ggplot(finalVar,aes(x='hour',y='mean',color='rain')) + geom_line() + ggtitle('Mean ridership counts for day hours')

# print(plot)