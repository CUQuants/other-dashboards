# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:53:47 2022

@author: Diego Alvarez
"""

import gspread
import pandas as pd
import datetime as dt

from gspread_dataframe import set_with_dataframe
from yield_curve_data_manager import *

data_manager = DataManager()
output_df = data_manager.output_df.reset_index()

sa = gspread.service_account(filename = "service_account.json")
sheet = sa.open("yield_curve")

def output(output_df):

    try:
        worksheet = sheet.worksheet("output")
        set_with_dataframe(worksheet, output_df)
        print(colored("[INFO]", "green"), "Data Written to Google Sheets")
        
    except:
        print(colored("[URGENT]", "red"), "Data Could Not be Written to Google Sheets")

def backend_output():

    try:
        worksheet = sheet.worksheet("backendInfo")
        today_date = dt.date.today()
        backend_dictionary = {"date": today_date, "timestamp": time.time()}
        backend_df = pd.DataFrame(data = backend_dictionary, index = [i for i in range(len(backend_dictionary))])
        set_with_dataframe(worksheet, backend_df)
        print(colored("[INFO]", "green"), "Backend Data Written to Google Sheets")
        
    except:
        print(colored("[URGENT]", "red"), "Backend Data Could Not be Written to Google Sheets")
        
def main():
    
    output(output_df)
    backend_output()
    
if __name__ == "__main__":
    main()