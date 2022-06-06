# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:53:47 2022

@author: Diego Alvarez
#went to configurations and changed the runtime
"""

import os
import gspread
import pandas as pd
import datetime as dt

from gspread_dataframe import set_with_dataframe
from yield_curve_amazon.yield_curve_data_manager import *

class YieldCurve:

    def __init__(self):
        
        self.data_manager = DataManager()
        self.output_df = self.data_manager.output_df.reset_index()

        self.sa = gspread.service_account(filename = "./yield_curve_amazon/service_account.json")
        self.sheet = self.sa.open("yield_curve")
        
        self.output()
        self.backend_output()

    def output(self):
    
        try:
            worksheet = self.sheet.worksheet("output")
            set_with_dataframe(worksheet, self.output_df)
            print("[INFO] Data Written to Google Sheets")
            
        except:
            print("[URGENT] Data Could Not be Written to Google Sheets")
    
    def backend_output(self):
    
        try:
            worksheet = self.sheet.worksheet("backendInfo")
            today_date = dt.date.today()
            backend_dictionary = {"date": today_date, "timestamp": time.time()}
            backend_df = pd.DataFrame(data = backend_dictionary, index = [i for i in range(len(backend_dictionary))])
            set_with_dataframe(worksheet, backend_df)
            
            print("[INFO] Backend Data Written to Google Sheets")
            
        except:
            print("[URGENT] Backend Data Could Not be Written to Google Sheets")