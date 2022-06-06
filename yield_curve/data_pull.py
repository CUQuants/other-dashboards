# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:45:06 2022

@author: Diego Alvarez
"""

import datetime as dt
import pandas_datareader as web

end_date = dt.date.today()
start_date = dt.date(end_date.year - 50, end_date.month, end_date.day)

tickers = ["DGS3MO", "DGS2", "DGS10", "T10Y2Y"]
df = web.DataReader(tickers, "fred", start_date, end_date).dropna()
df.to_csv("yield_curve_data.csv")