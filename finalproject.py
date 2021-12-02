# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:11:20 2021

@author: lenovo
"""

# project final
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


japan_data = pd.read_csv('pcr_case_daily.csv')
ourworld_testperconfirme = pd.read_csv('tests_per_confirmed_case.csv')
ourworld_dailyvac = pd.read_csv('daily-covid-vaccination-doses-per-capita.csv')
positiverate = pd.read_csv('positive-rate-daily-smoothed.csv')

type(japan_data)
japan_data.columns[2]
japan_data.quarantine_station
type(japan_data.quarantine_station)
japan_data.quarantine_station.iloc[126:205]
type(japan_data.quarantine_station.iloc[126:205])
type(japan_data.date)

date_olympic = japan_data.date.iloc[469:522]
quarantine_olympic = japan_data.quarantine_station.iloc[469:522]
total_olympic = japan_data.total.iloc[469:522]
index = np.arange(0,17)
width = 0.4 
plt.plot(date_olympic,total_olympic)
plt.plot(date_olympic,quarantine_olympic)
plt.title("PCR test daily")
plt.xlabel("Date (1/6/21 to 22/7/21)")
plt.xticks(rotation=60,visible=False)
plt.ylabel("population")
plt.legend(['total','quarantine'])
plt.show()





date_olympic_ourworld = ourworld_testperconfirme.Day.iloc[27673:27725]
tests_per_confirmed_case = ourworld_testperconfirme.short_term_tests_per_case.iloc[27673:27725]
plt.plot(date_olympic_ourworld,tests_per_confirmed_case)
plt.title("Test Per Confiremed Cases")
plt.xlabel("Date (1/6/21 to 22/7/21) ")
plt.ylabel("test per confiremed cases")
plt.xticks(visible=False)







dailyvac = ourworld_dailyvac.new_vaccinations_smoothed_per_million.iloc[28465:28517]
date_vacdaily = ourworld_dailyvac.Day.iloc[28465:28517]
plt.plot(date_vacdaily ,dailyvac)
plt.title("new_vaccinations_per_million(before 1 month)")
plt.xlabel("Date (1/6/21 to 22/7/21)")
plt.ylabel("new_vaccinations_per_million")
plt.xticks(rotation=70,visible=False)




plt.plot(positiverate.Day.iloc[28416:28467],positiverate.short_term_positivity_rate.iloc[28416:28467])
plt.title("The Positive Rate")
plt.xlabel("Date (1/6/21 to 22/7/21)")
plt.ylabel("Positive Rate(%population)")
plt.xticks(visible=False)




