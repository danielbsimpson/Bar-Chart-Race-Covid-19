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

data = pd.read_csv("C:/Users/Damien/Desktop/Data Science/Data Science Projects/Covid/us-counties.csv")
data['date'] = pd.to_datetime(data['date'])
data = data.drop(columns = ['fips', 'county'])
data['month'] = data['date'].dt.strftime('%b')

#Assign a color for every state for use in matplotlib
state_list = list(data['state'].unique())
color_list = ['#7e1e9c', '#15b01a', '#0343df', '#ff81c0', '#653700', '#e50000',
              '#95d0fc', '#029386', '#f97306', '#96f97b', '#c20078', '#ffff14',
              '#929591', '#89fe05', '#75bbfd', '#bf77f6', '#9a0eea', '#03719c',
              '#06c2ac', '#c79fef', '#00035b', '#d1b26f', '#00ffff', '#13eac9',
              '#a9f971', '#ae7181', '#ed0dd9', '#01ff07', '#650021', '#6e750e',
              '#ff796c', '#e6daa6', '#0504aa', '#a2cffe', '#cea2fd', '#840000',
              '#ff028d', '#ad8150', '#c7fdb5', '#ffb07c', '#677a04', '#cb416b',
              '#8e82fe', '#53fca1', '#aaff32', '#380282', '#ceb301', '#ffd1df',
              '#cf6275', '#0165fc']
state_color = dict(zip(state_list, color_list))

#Sum all the data up to the date specified
def get_week(data, date):
    desired_week = data[data['date'] == date].groupby('state').agg({
        'cases':'sum','deaths':'sum'})
    cases_week = desired_week.nlargest(10, 'cases')
    deaths_week = desired_week.nlargest(10, 'deaths')
    
    return (cases_week, deaths_week)

#Added in zero values to ensure Bar Chart is same length for every week
jan_cases = get_week(data, '2020-01-31')[0]
jan_cases.loc['Massachusetts'] = [0,0]
jan_cases.loc['Wisconsin'] = [0,0]
jan_cases.loc['Texas'] = [0,0]
jan_cases.loc['Nebraska'] = [0,0]
jan_cases.loc['Utah'] = [0,0]
jan_cases.loc['Oregon'] = [0,0]
jan_cases['month'] = 'January'

feb_cases1 = get_week(data, '2020-02-08')[0]
feb_cases1.loc['Texas'] = [0,0]
feb_cases1.loc['Nebraska'] = [0,0]
feb_cases1.loc['Utah'] = [0,0]
feb_cases1.loc['Oregon'] = [0,0]
feb_cases1['month'] = 'February'

feb_cases2 = get_week(data, '2020-02-15')[0]
feb_cases2.loc['Nebraska'] = [0,0]
feb_cases2.loc['Utah'] = [0,0]
feb_cases2.loc['Oregon'] = [0,0]
feb_cases2['month'] = 'February'

feb_cases3 = get_week(data, '2020-02-22')[0]
feb_cases3.loc['Oregon'] = [0,0]
feb_cases3.loc['Utah'] = [0,0]
feb_cases3['month'] = 'February'

feb_cases4 = get_week(data, '2020-02-29')[0]
feb_cases4['month'] = 'February'

mar_cases1 = get_week(data, '2020-03-07')[0]
mar_cases1['month'] = 'March'
mar_cases2 = get_week(data, '2020-03-14')[0]
mar_cases2['month'] = 'March'
mar_cases3 = get_week(data, '2020-03-21')[0]
mar_cases3['month'] = 'March'
mar_cases4 = get_week(data, '2020-03-28')[0]
mar_cases4['month'] = 'March'


apr_cases1 = get_week(data, '2020-04-04')[0]
apr_cases1['month'] = 'April'
apr_cases2 = get_week(data, '2020-04-11')[0]
apr_cases2['month'] = 'April'
apr_cases3 = get_week(data, '2020-04-18')[0]
apr_cases3['month'] = 'April'
apr_cases4 = get_week(data, '2020-04-25')[0]
apr_cases4['month'] = 'April'

may_cases1 = get_week(data, '2020-05-02')[0]
may_cases1['month'] = 'May'
may_cases2 = get_week(data, '2020-05-09')[0]
may_cases2['month'] = 'May'
may_cases3 = get_week(data, '2020-05-16')[0]
may_cases3['month'] = 'May'
may_cases4 = get_week(data, '2020-05-23')[0]
may_cases4['month'] = 'May'
may_cases5 = get_week(data, '2020-05-30')[0]
may_cases5['month'] = 'May'

june_cases1 = get_week(data, '2020-06-06')[0]
june_cases1['month'] = 'June'
june_cases2 = get_week(data, '2020-06-13')[0]
june_cases2['month'] = 'June'
june_cases3 = get_week(data, '2020-06-20')[0]
june_cases3['month'] = 'June'
june_cases4 = get_week(data, '2020-06-27')[0]
june_cases4['month'] = 'June'

july_cases1 = get_week(data, '2020-07-03')[0]
july_cases1['month'] = 'July'
july_cases2 = get_week(data, '2020-07-10')[0]
july_cases2['month'] = 'July'
july_cases3 = get_week(data, '2020-07-17')[0]
july_cases3['month'] = 'July'
july_cases4 = get_week(data, '2020-07-24')[0]
july_cases4['month'] = 'July'
july_cases5 = get_week(data, '2020-07-31')[0]
july_cases5['month'] = 'July'

aug_cases1 = get_week(data, '2020-08-07')[0]
aug_cases1['month'] = 'August'
aug_cases2 = get_week(data, '2020-08-14')[0]
aug_cases2['month'] = 'August'
aug_cases3 = get_week(data, '2020-08-21')[0]
aug_cases3['month'] = 'August'
aug_cases4 = get_week(data, '2020-08-28')[0]
aug_cases4['month'] = 'August'

sep_cases1 = get_week(data, '2020-09-04')[0]
sep_cases1['month'] = 'September'
sep_cases2 = get_week(data, '2020-09-11')[0]
sep_cases2['month'] = 'September'
sep_cases3 = get_week(data, '2020-09-18')[0]
sep_cases3['month'] = 'September'
sep_cases4 = get_week(data, '2020-09-25')[0]
sep_cases4['month'] = 'September'

#Place all the weeks into a list
weeks_list = [jan_cases, feb_cases1, feb_cases2, feb_cases3, feb_cases4, mar_cases1,
              mar_cases2, mar_cases3, mar_cases4, apr_cases1, apr_cases2, 
              apr_cases3, apr_cases4, may_cases1, may_cases2, may_cases3, 
              may_cases4, may_cases5, june_cases1, june_cases2, june_cases3, 
              june_cases4, july_cases1, july_cases2, july_cases3, july_cases4,
              july_cases5, aug_cases1, aug_cases2, aug_cases3, aug_cases4,
              sep_cases1, sep_cases2, sep_cases3, sep_cases4]

#Plot for cases bar chart
def cases_plot(week):
    week = week[::-1]
    state_list = list(week.index.values)
    fig, ax = plt.subplots(figsize=(15, 8))
    plt.style.use('seaborn')

    ax.barh(state_list, week['cases'], color=[state_color[x] for x in state_list])
    for i, (value, name) in enumerate(zip(week['cases'], state_list)):
        ax.text(value, i,     name,size=18, weight=600, ha='left', va='bottom')
        ax.text(value, i -.25, f'{value:,.0f}',  size=14, ha='right',  va='center')
    
    ax.text(0, 1.12, 'Covid-19 total reported cases by state',
        transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.text(1, 0.4, week['month'][0], transform=ax.transAxes, size=46, ha='right')
    ax.set_axisbelow(True)

#Plot for deaths bar chart
def deaths_plot(week):
    week = week[['deaths', 'month']]
    week = week.sort_values('deaths')
    state_list = list(week.index.values)
    fig, ax = plt.subplots(figsize=(15, 8))
    plt.style.use('seaborn')

    ax.barh(state_list, week['deaths'], color=[state_color[x] for x in state_list])
    for i, (value, name) in enumerate(zip(week['deaths'], state_list)):
        ax.text(value, i,     name,size=18, weight=600, ha='left', va='bottom')
        ax.text(value, i -.25, f'{value:,.0f}',  size=14, ha='right',  va='center')
    
    ax.text(0, 1.12, 'Covid-19 total reported deaths by state',
        transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.text(1, 0.4, week['month'][0], transform=ax.transAxes, size=46, ha='right')
    ax.set_axisbelow(True)
    
#Loop through all weeks to create multiple plots
def create_cases_plots():
    for i in range(0, len(weeks_list)):
        cases_plot(weeks_list[i])
def create_deaths_plots():    
    for i in range(0, len(weeks_list)):
        deaths_plot(weeks_list[i])
    

#Animationed version
'''
from matplotlib.animation import FuncAnimation 
fig, ax = plt.subplots(figsize=(15, 8))
MyAnimation = FuncAnimation(fig, get_plot, frames=weeks_months)
#MyAnimation.save('Animation.gif', writer='imagemagick')
#HTML(MyAnimation.to_jshtml())
#MyAnimation.to_html5_video()
'''
