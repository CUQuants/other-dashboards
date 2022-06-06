# -*- coding: utf-8 -*-
"""
Created on Wed May 18 00:04:12 2022

@author: Diego
"""

import gspread
import pandas as pd
import datetime as dt

from gspread_dataframe import set_with_dataframe
from data_manager import *

sa = gspread.service_account(filename = "service_account.json")
sheet = sa.open("yield_curve")

worksheet = sheet.worksheet("output")
set_with_dataframe(worksheet, output_df)
print(colored("[INFO]", "green"), "Data Written to Google Sheets")