# API Key for Alpha Vantage: D1UA2DG18SPT7MCN
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

key = 'D1UA2DG18SPT7MCN'


def dailyPivotInfo(symbol):  # gotta figure out how to parse of the daily info..
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    high = data.iloc[0, 1]  # ['1. open', '2. high', '3. low', '4. close', '5. volume']
    low = data.iloc[0, 2]
    close = data.iloc[0, 3]
    pivotPointCalculation = (high + low + close) / 3
    pivotPoint = round(pivotPointCalculation, 2)
    print(pivotPoint)
    return pivotPoint

def weeklyPivotInfo(symbol):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_weekly(symbol=symbol)
    high = data.iloc[1, 1]  # ['1. open', '2. high', '3. low', '4. close', '5. volume']
    low = data.iloc[1, 2]
    close = data.iloc[1, 3]
    pivotPointCalculation = (high + low + close) / 3
    pivotPoint = round(pivotPointCalculation, 2)
    print(pivotPoint)
    return pivotPoint


#weeklyPivotInfo('amd')


def monthlyPivotInfo(symbol):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_monthly(symbol=symbol)
    high = data.iloc[1, 1]  # ['1. open', '2. high', '3. low', '4. close', '5. volume']
    low = data.iloc[1, 2]
    close = data.iloc[1, 3]
    pivotPointCalculation = (high + low + close) / 3
    pivotPoint = round(pivotPointCalculation, 2)
    print(pivotPoint)
    return pivotPoint


# print(monthlyPivotInfo('amd'))
# print('weekly info')
# print(weeklyPivotInfo('amd'))

def stockQuote(symbol):  # still gotta figure out how to parse
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_quote_endpoint(symbol=symbol)
    print(data)

# stockQuote('amd')



#make a list of your 'watchlist'.... figure out if it is a correct stock name... if it is correct add to the watch list.