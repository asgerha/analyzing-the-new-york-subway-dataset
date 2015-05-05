import numpy as np
import pandas
import r_squared
from ggplot import *


df = pandas.read_csv('/Users/aha/Documents/workspace/udacity/p1/turnstile_weather_v2.csv')
countName = 'ENTRIESn_hourly'

rainy = df[df.rain == 1]
notRainy = df[df.rain == 0]

binwidth = 500
limits = [0,15000]

plot1 = ggplot(notRainy, aes(countName)) \
+ ggtitle('Subways riders on non-rainy days') \
+ labs("ENTRIESn_hourly", "Frequency") \
+ scale_x_continuous(limits=limits) + geom_histogram(binwidth=binwidth) 
print(plot1)

plot2 = ggplot(rainy, aes(x=countName)) \
+ ggtitle('Subways riders on rainy days') \
+ labs("ENTRIESn_hourly", "Frequency") \
+ scale_x_continuous(limits=limits) + geom_histogram(binwidth=binwidth)

print(plot2)

# plot2 = ggplot(cost_df, aes('Ridership counts', 'Frequency')) + \
#       geom_point() + ggtitle('Cost History for alpha = %.3f' % 1 )