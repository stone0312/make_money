#!/usr/bin/env python3
"""
============================================================================
 File:	      find_turning_point_2nd.py
 Description: modify the vel model 
 Author:      stone
 date:        2021.04.03
 Website:     https://github.com/stone0312/make_money_github.git
 Version:     2.0
 Note:        put data into numpy and analysis

============================================================================
"""

import matplotlib.pyplot as plt
import tushare as ts
import pandas  as pd
import numpy   as np
from datetime import datetime

#for tushare_api 

pro = ts.pro_api('66c23a5bc715738d70b6f7d7a0a936b94b31e1254fa4c32a902d8c48')

#define par

your_want   = 'pct_chg'
label_name1 = 'wine'
label_name2 = 'yao'

#======================================================================================
def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)

    re = np.convolve(interval, window, 'same')

    return re
#======================================================================================
def get_data():
    
    data = pd.read_csv('~/make_money_github/data/stock1.csv')
    data2 = pd.read_csv('~/make_money_github/data/stock2.csv')
    data_pct = data[your_want]
    data_pct2 = data2[your_want]

    data_m5 = moving_average(data_pct , 5)
    data_my5 = moving_average(data_pct2 , 5)
    
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title('original')
    plt.plot(data_pct,color = 'red', label = label_name1)
    plt.plot(data_pct2,color = 'blue', label = label_name2)
    plt.xlabel('date')
    plt.ylabel('pct')
    plt.legend(loc='upper right')
    

    plt.subplot(2,1,3)
    plt.title('mv5')
    plt.plot(data_m5, color = 'red',label = label_name1)
    plt.plot(data_my5, color = 'blue',label = label_name2)
    plt.xlabel('date')
    plt.ylabel('pct')
    plt.legend(loc='upper right')

    plt.show()

#======================================================================================
def real_main():
    get_data()

#======================================================================================
if __name__ == "__main__":
    real_main()

