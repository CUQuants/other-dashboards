# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:45:06 2022

@author: Diego Alvarez
"""

import os
import sys
import time
import requests
import datetime as dt
import pandas_datareader as web

from termcolor import colored

class DataManager():

    def __init__(self):
        
        if self.check_internet_connection() == False:
            sys.exit()
            
        if self.check_json() == False:
            sys.exit()
            
        if self.collect_data() == False:
            sys.exit()
            
        if self.computation() == False:
            sys.exit()

    def check_internet_connection(self):
        
        url = "https://www.google.com"
        try:
            test_requests = requests.get(url, timeout = 5)
            print(colored("[INFO]", "green"), "Internet Connection Established")
            return True
        
        except:
            print(colored("[URGENT]", "red"), "Internet Connection Not Established")
            return False
        
    def check_json(self):

        cwd = os.getcwd()
        
        for i in os.listdir(cwd):
            
            file_ending = i
            file_ending = i.split(".")
            
            try:
                if(file_ending[1] == "json"):
                    print(colored("[INFO]", "green"), "JSON Found Using:",i)
                    return True
            except:
                pass
            
        print(colored("[URGENT]", "red"), "JSON Not Found")
        return False
    
    #need a file that checks that there is an AWS connection
    
    def collect_data(self):
        
        try:
            
            end_date = dt.date.today()
            start_date = dt.date(end_date.year - 50, end_date.month, end_date.day)
    
            tickers = ["DGS3MO", "DGS2", "DGS10", "T10Y2Y"]
            self.df = web.DataReader(tickers, "fred", start_date, end_date).dropna()
            
            print(colored("[INFO]", "green"), "Collected Data")
            return True
        
        except:
            
            print(colored("[URGENT]", "red"), "Data Could Not Be Collected")
            return False
        
    def computation(self):
        
        try:
        
            start_time = time.time()
            self.df.columns = ["3MONTH", "2YEAR", "10YEAR", "10YEAR-2YEAR"]
            self.df["10YEAR-3MONTH"] = self.df["10YEAR"] - self.df["3MONTH"]
            self.output_df = self.df[["10YEAR-2YEAR", "10YEAR-3MONTH"]]
            end_time = time.time()
            comp_time = end_time - start_time
            
            print(colored("[INFO]", "green"), "Compuatation Completed in:", comp_time,"seconds")
            return True
        
        except:
            
            print(colored("[URGENT]", "red"), "Computation Could Not Be Completed")
            return False
    
    

        
            

