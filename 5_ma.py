#!/usr/bin/env python3

'''
2021-03-10
test 5-ma moudle
copyright by sy
'''
import matplotlib.pyplot as plt
import tushare as ts
import pandas as pd
from datetime import datetime

#for tushare_api 

pro = ts.pro_api('66c23a5bc715738d70b6f7d7a0a936b94b31e1254fa4c32a902d8c48')

#define par

stock_code = input('please enter the code(like 000858.SZ):\n')
start_date = input('please enter the start date(like 20200101):\n')
end_date = input('please enter the end date(like 20200101):\n')

#======================================================================================
def MA5_talib():
    df = pro.daily(ts_code=stock_code,start_date=start_date,end_date=end_date)
    df2 = df.sort_values(by='trade_date', ascending=True)
    df2['MA5_rolling'] = df['close'].rolling(window=5).mean()
    df2['MA10_rolling'] = df['close'].rolling(window=10).mean()
    df2.to_csv('~/make_money/ma.csv')
    plt.plot(df2['trade_date'],df2['MA5_rolling'],label = 'MA5')
    plt.plot(df2['trade_date'],df2['MA10_rolling'],color='blue',label = 'MA10')
    plt.plot(df2['trade_date'],df2['close'],color='red',label = 'close')
    plt.xticks(rotation=90)

    #set label

    plt.xlabel('date')
    plt.ylabel('price')

    #set legend

    plt.legend(loc='upper right')

    plt.show()
#======================================================================================
def real_main():
    MA5_talib()

#======================================================================================
if __name__ == "__main__":
    real_main()

