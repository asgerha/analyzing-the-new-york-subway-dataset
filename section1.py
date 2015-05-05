import numpy as np
import scipy as sp
import pandas
from pandas import DataFrame, Series
from ggplot import *
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_weather_v2.csv')
# df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_data_master_with_weather.csv')


# stk_list = ['AQUEDUCT TRACK','ORCHARD BEACH','WILSON AVE','191 ST','181 ST']
# stk_list = []
# df = df[~df['station'].isin(stk_list)]

# stationNames = pandas.unique(df['station'])
# print(df[df['station'].isin(stk_list)])

# rainCount= 9585

countName = 'ENTRIESn_hourly'
colNames =[countName]

rainy = df[df.rain == 1][colNames]
notRainy = df[df.rain == 0][colNames]

rainyAr= rainy[countName]
notRainyAr=notRainy[countName]

meanRainy =  np.mean(rainyAr)
meanNotRainy =  np.mean(notRainyAr)

# notRainy['datetime'] = notRainy['datetime'].astype('datetime64')
# notRainy = notRainy.sort_index(by=['datetime', countName])

U,p =sp.stats.mannwhitneyu(rainyAr,notRainyAr)
print("U: "+str(U) + " p: " + str(p) + '\n' + 'Rainy day Mean: '+ str(meanRainy) +' Not rainy day mean: '+ str(meanNotRainy))
# print(rainy.info())

# pandas.DataFrame(stationNames).to_csv('/Users/aha/Documents/workspace/udacity/p1/notRainy.csv')
# h = np.histogram(notRainy)

# print(df.info())
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