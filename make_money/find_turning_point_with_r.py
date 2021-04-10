#!/usr/bin/env python3
"""
============================================================================
 File:	      find_turning_point_with_r.py
 Description: use correlation to find turning point 
 Author:      stone
 date:        2021.04.10
 Website:     https://github.com/stone0312/make_money_github.git
 Version:     1.0
 Note:        can not be used directly

============================================================================
"""

import matplotlib.pyplot as plt
import tushare as ts
import pandas as pd
from datetime import datetime

#for tushare_api 

pro = ts.pro_api('66c23a5bc715738d70b6f7d7a0a936b94b31e1254fa4c32a902d8c48')

#define par

stock_code1 = '600809.SH'
stock_code2 = '600744.SH'
start_date  = '20210301'
end_date    = '20210402'
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

    df = pro.daily(ts_code=stock_code1,start_date=start_date,end_date=end_date)
    df = df.sort_values(by='trade_date', ascending=True)
  # df.to_csv('~/make_money_github/data/stock1.csv')
    plt.xticks(rotation=90)

    df2 = pro.daily(ts_code=stock_code2,start_date=start_date,end_date=end_date)
    df2 = df2.sort_values(by='trade_date', ascending=True)
  # df2.to_csv('~/make_money_github/data/stock2.csv')
    plt.xticks(rotation=90)

#======================================================================================
#def draw():

    plt.plot(df['trade_date'],df[your_want],color='blue',label = label_name1)
    plt.plot(df2['trade_date'],df2[your_want],color='red',label = label_name2)

    #set label

    plt.xlabel('date')
    plt.ylabel('price')

    #set legend

    plt.legend(loc='upper right')

    plt.show()
#======================================================================================
def real_main():
    get_data()


#======================================================================================
if __name__ == "__main__":
    real_main()

