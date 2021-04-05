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
stock_code1 = '000858.SZ'
stock_code2 = '600744.SH'
start_date  = '20210101'
end_date    = '20210218'
supertitle  = 'from 2021-1-1 to 2021-2-19'
#======================================================================================
def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)

    re = np.convolve(interval, window, 'same')

    return re
#======================================================================================
def draw():
    
    #get_data

    df1 = pro.daily(ts_code=stock_code1,start_date=start_date,end_date=end_date)
    df1 = df1.sort_values(by='trade_date', ascending=True)
    df1.to_csv('~/make_money_github/data/stock1.csv')
    
    df2 = pro.daily(ts_code=stock_code2,start_date=start_date,end_date=end_date)
    df2 = df2.sort_values(by='trade_date', ascending=True)
    df2.to_csv('~/make_money_github/data/stock2.csv')
   
    #save_data
    data = pd.read_csv('~/make_money_github/data/stock1.csv')
    data2 = pd.read_csv('~/make_money_github/data/stock2.csv')
    data_pct = data[your_want]
    data_pct2 = data2[your_want]

    data_m5 = moving_average(data_pct , 5)
    data_my5 = moving_average(data_pct2 , 5)
    
    plt.figure(1)
    plt.suptitle(supertitle)
    plt.subplot(2,1,1)
    plt.title('original')
    plt.plot(data_pct,color = 'red', label = label_name1)
    plt.plot(data_pct2,color = 'blue', label = label_name2)
    plt.xlabel('date')
    plt.ylabel('pct')
    plt.legend(loc='upper right')
    

    plt.subplot(2,1,2)
    plt.title('mv5')
    plt.plot(data_m5, color = 'red',label = label_name1)
    plt.plot(data_my5, color = 'blue',label = label_name2)
    plt.xlabel('date')
    plt.ylabel('pct')
    plt.legend(loc='upper right')

    plt.show()

#======================================================================================
def real_main():
    draw()

#======================================================================================
if __name__ == "__main__":
    real_main()

