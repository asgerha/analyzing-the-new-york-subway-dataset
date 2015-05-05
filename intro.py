import numpy as np
import scipy as sp
import pandas
from pandas import DataFrame, Series
from ggplot import *
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_weather_v2.csv')

#print(df[['UNIT','ENTRIESn','datetime']])
stationNames = pandas.unique(df['station'])
# print(stationNames)

rainCount= 9585

countName = 'ENTRIESn_hourly'
colNames =['station',countName,'datetime']

rainy = df[df.rain == 1][colNames]
notRainy = df[df.rain == 0][colNames]

rainyAr= rainy[countName]
notRainyAr=notRainy[countName]

meanRainy =  np.mean(rainyAr)
meanNotRainy =  np.mean(notRainyAr)

notRainy['datetime'] = notRainy['datetime'].astype('datetime64')
notRainy = notRainy.sort_index(by=['datetime', countName])

U,p =sp.stats.mannwhitneyu(rainyAr,notRainyAr)
print(str(U) + " " + str(p) + '\n' + 'rainMean: '+ str(meanRainy) +' meanNotRainy: '+ str(meanNotRainy))
# print(rainy.info())

# pandas.DataFrame(stationNames).to_csv('/Users/aha/Documents/workspace/udacity/p1/notRainy.csv')
# h = np.histogram(notRainy)

# print(df)
# p = ggplot(notRainy,aes(x='datetime',y=countName,colour='station')) + geom_line()

# p= ggplot(aes(x='date', y='beef'), data=meat) + \
# geom_point(color='lightblue') + \
# stat_smooth(span=.15, color='black', se=True) + \
# ggtitle("Beef: It's What's for Dinner") + \
# xlab("Date") + \
# ylab("Head of Cattle Slaughtered")
# print(p)

# 153635120.5 2.74106957124e-06
# rainMean: 2028.19603547 meanNotRainy: 1845.53943866

153635120.5 2.74106957124e-06
rainMean: 2028.19603547 meanNotRainy: 1845.53943866