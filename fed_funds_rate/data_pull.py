# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:28:32 2022

@author: Diego Alvarez
"""

#this is used to pass dates
import datetime as dt

#this is used to access the FRED (St. Louis Federal Reserve) Database 
import pandas_datareader as web

#this is for plotting to test out the data
import matplotlib.pyplot as plt

#today's date
end_date = dt.date.today()

#the graph uses annual values over the last 37 years
start_date = dt.date(end_date.year - 40, end_date.month, end_date.day)

#these are all of the values that we want to pull
tickers = ["FEDFUNDS", "IRLTLT01EZM156N", "IRLTLT01GBM156N", "IRLTLT01USM156N", "IRLTLT01JPM156N"]

#this will get us all of the rate, I dropna to clean the data and take percentage change and then dropNA again
df = web.get_data_fred(tickers, start_date, end_date).dropna().pct_change().dropna()

#save all of the data because we don't want keep rerunning this file because it pulls the data each time
df.to_csv("data.csv")
