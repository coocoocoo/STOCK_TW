# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:55:53 2017

@author: shawn
"""

import os 
import datetime
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

file_path = '/Users/shawn/Dropbox/GitHubCode/StockAnalysis'
os.chdir(file_path)
CRT_date = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M')
#logging.basicConfig(filename=['/log/'+ CRT_date+'.txt'])

data = pd.read_csv(file_path + '/tsec/data/0050.csv', 
                    names=['date','deal_goo','deal_price','open','max','min','close','diff','deal_num'])



""" try catch error information
close = data['max']
for i in range(0,len(close)):
    try:
        print(float(close[i]))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("line:",i,'Value:',close[i])
        break
"""
