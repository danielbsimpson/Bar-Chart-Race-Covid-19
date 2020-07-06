# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:48:12 2020

@author: Daniel Simpson
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

data = pd.read_csv("C:/Users/Damien/Desktop/Data Science Projects/Covid/us-counties.csv")
data['date'] = pd.to_datetime(data['date'])
data = data.drop(columns = ['fips', 'county'])

def get_week(data, date):
    desired_week = data[data['date'] == date].groupby('state').agg({'cases':'sum'})
    desired_week = desired_week.nlargest(10, 'cases')
    return desired_week

jan_week = get_week(data, '2020-01-31')
jan_week.loc['Massachusetts'] = [0]
jan_week.loc['Wisconsin'] = [0]
jan_week.loc['Texas'] = [0]
jan_week.loc['Nebraska'] = [0]
jan_week.loc['Utah'] = [0]
jan_week.loc['Oregon'] = [0]

feb_week1 = get_week(data, '2020-02-08')
feb_week1.loc['Texas'] = [0]
feb_week1.loc['Nebraska'] = [0]
feb_week1.loc['Utah'] = [0]
feb_week1.loc['Oregon'] = [0]

feb_week2 = get_week(data, '2020-02-15')
feb_week2.loc['Nebraska'] = [0]
feb_week2.loc['Utah'] = [0]
feb_week2.loc['Oregon'] = [0]

feb_week3 = get_week(data, '2020-02-22')
feb_week3.loc['Oregon'] = [0]
feb_week3.loc['Utah'] = [0]

feb_week4 = get_week(data, '2020-02-29')

mar_week1 = get_week(data, '2020-03-07')
mar_week2 = get_week(data, '2020-03-14')
mar_week3 = get_week(data, '2020-03-21')
mar_week4 = get_week(data, '2020-03-28')

apr_week1 = get_week(data, '2020-04-04')
apr_week2 = get_week(data, '2020-04-11')
apr_week3 = get_week(data, '2020-04-18')
apr_week4 = get_week(data, '2020-04-25')

may_week1 = get_week(data, '2020-05-02')
may_week2 = get_week(data, '2020-05-09')
may_week3 = get_week(data, '2020-05-16')
may_week4 = get_week(data, '2020-05-23')
may_week5 = get_week(data, '2020-05-30')

june_week1 = get_week(data, '2020-06-06')
june_week2 = get_week(data, '2020-06-13')
june_week3 = get_week(data, '2020-06-20')
june_week4 = get_week(data, '2020-06-27')

july_week1 = get_week(data, '2020-07-03')

weeks_list = [jan_week, feb_week1, feb_week2, feb_week3, feb_week4, mar_week1,
              mar_week2, mar_week3, mar_week4, apr_week1, apr_week2, 
              apr_week3, apr_week4, may_week1, may_week2, may_week3, 
              may_week4, may_week5, june_week1, june_week2, june_week3, 
              june_week4, july_week1]

months_list = ['January', 'February', 'February', 'February', 'February', 
               'March', 'March', 'March', 'March', 'April', 'April', 'April', 
               'April', 'May', 'May', 'May', 'May', 'May', 'June', 'June', 
               'June', 'June', 'July']

def get_plot(week, month):
    week = week[::-1]
    state_list = list(week.index.values)
    fig, ax = plt.subplots(figsize=(15, 8))

    ax.barh(state_list, week['cases'])
    for i, (value, name) in enumerate(zip(week['cases'], state_list)):
        ax.text(value, i,     name,size=14, weight=600, ha='left', va='bottom')
        ax.text(value, i -.25, f'{value:,.0f}',  size=14, ha='right',  va='center')
    
    ax.text(0, 1.12, 'Covid-19 total reported cases by state',
        transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.text(1, 0.4, month, transform=ax.transAxes, size=46, ha='right')
    ax.set_axisbelow(True)

for i in range(0, len(weeks_list)):
    get_plot(weeks_list[i], months_list[i])

'''
from matplotlib.animation import FuncAnimation 
fig, ax = plt.subplots(figsize=(15, 8))
MyAnimation = FuncAnimation(fig, get_plot, frames=weeks_months)

#MyAnimation.save('Animation.gif', writer='imagemagick')
#HTML(MyAnimation.to_jshtml())
#MyAnimation.to_html5_video()
'''