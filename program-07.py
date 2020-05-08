#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 00:50:39 2020

@author: Mukhamad Suhermanto
HW7 - Data Analysis
"""
# Importing relevant packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
import scipy.stats as stats

df = pd.read_csv('all_month.csv', #opening the file
                 delimiter = ',') #using the delimiter
df.head() #Checking the head only
#Trying to plot without modifying the NaN
''' 
plt.hist(df['mag'], bins=10, range=(0,10))
plt.xlabel('Magnitude', size=10)
plt.ylabel('Frequency', size=10)

'''
#making a graph without dropping NaN (Not available Number) will cause trouble like this

# Removing NaN data, since it will trouble the plot process
#md_df is modified dataframe
mod_df = df.dropna(axis = 0, subset = ['mag'])
#print(df)
#print(mod_df)

# 2.2 Histogram / Bar Plot
plt.figure(1)
plt.hist(mod_df['mag'], 
         bins=10, # bins size
         range=(0,10), #range as per instruction
         color='g', # bar color
         edgecolor='k') # edgecolor -> edge of the bar for more distinctive result
plt.xlabel('Magnitude', size=10)
plt.ylabel('Frequency', size=10)
plt.title('2.2 Earthquake Magnitudes and its Frequency')

# 2.3 KDE plot, with Gaussian kernel, width 0.2
plt.figure(2)
sns.set_style('darkgrid')
sns.kdeplot(np.array(mod_df['mag']), #input is in array
            kernel='gau', #using Gaussian Kernel
            bw=0.2, #width
            shade= True) #the shade under the plot line
plt.xlabel('Magnitude', size=10)
plt.ylabel('Density', size=10)
plt.title('2.3 KDE Plot of Earthquake Magnitude', size=12)

#to check the relation of KDE vs Histogram
plt.figure(3)
sns.distplot(mod_df['mag'], bins=10, kde=True)

# 2.4. Plot latitude versus longitude for all earthquakes
plt.figure(4)
plt.scatter(mod_df['longitude'], #longitude as the x-axis input
            mod_df['latitude'],  #latitiude as the y-axis input
            c='r', marker='+') # the points is shown in red +
plt.xlabel('Longitude', size=10)
plt.ylabel('Latitude', size=10)
plt.title('2.4 Latitude vs Longitude of All Earthquakes', size=14, c='b')

# 2.5 The normalized cumulative distribution plot of earthquake depths 
plt.figure(5)
plt.hist(mod_df['depth'], 
         bins=100,
         cumulative=True,#cumulative
         normed=True, #normalized --> this shows warning that kwarg no longer use normed, instead density
         color='g', #line color is green
         histtype='step') #type of histogram used
plt.xlabel('Depth [km]', size=10)
plt.ylabel('Cumulative Proportion of All Sites', size=10)
plt.title('2.5 CFD of Earthquake Depth', size='14', c='b')

#2.6 The scatter plot of magnitude as a function of the depth
plt.figure(6)
plt.scatter(mod_df['mag'], #magnitude as the x-axis 
            mod_df['depth'], #depth as the y-axis 
            c='g', #color of the earthquake
            marker='*')#marker
plt.xlabel('Magnitude', size=10)
plt.ylabel('Depth [km]', size=10)
plt.title('2.6 Earthquake Magnitude and Depth', size='14', c='b')

#2.7 Statistical probability plot / # Q-Q plot using scipy.stats.probplot
plt.figure(7)
stats.probplot(mod_df['mag'], #the data to be called
               dist='norm', #using normal distribution
               plot=pylab) #plot using pylab
