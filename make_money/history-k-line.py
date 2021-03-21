#!/usr/bin/env python3

'''
2021-03-04
show history k-lines
copyright by sy
'''
import matplotlib.pyplot as plt
import tushare as ts
from datetime import datetime

#for tushare_api 

pro = ts.pro_api('66c23a5bc715738d70b6f7d7a0a936b94b31e1254fa4c32a902d8c48')

#define par

stock_code = input('please enter the code(like 000858.SZ):\n') 
start_date = input('please enter the start date(like 20210103):\n') 
end_date = input('please enter the end date(like 20210103):\n') 

#======================================================================================
def history_k_line():
# {{{
    df = pro.daily(ts_code=stock_code,start_date=start_date,end_date=end_date)
    df2 = df.sort_values(by='trade_date', ascending=True)
    df2.to_csv('~/make_money/date.csv')
    plt.plot(df2['trade_date'],df2['close'])
    plt.xticks(rotation=90)
    
    plt.show()
# }}}
#======================================================================================
def real_main():
    history_k_line()

#======================================================================================
if __name__ == "__main__":
    real_main()

