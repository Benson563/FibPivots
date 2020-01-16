# API Key for Alpha Vantage: D1UA2DG18SPT7MCN
import pandas as pd
import PivotCalculations
from alpha_vantage.timeseries import TimeSeries
import time

key = 'D1UA2DG18SPT7MCN'


def dailyPivotInfo(symbol):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    high = data.iloc[0, 1]  # ['1. open', '2. high', '3. low', '4. close', '5. volume']
    low = data.iloc[0, 2]
    close = data.iloc[0, 3]
    pivotList = PivotCalculations.fibPivot(high, low, close)
    return pivotList

#dailyPivotInfo('tsla')

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

def stockQuote(symbol):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_quote_endpoint(symbol)

    cPrice = data.iloc[0, 4]
    currentPrice = float(cPrice)
     # current price


# make a list of your 'watchlist'.... figure out if it is a correct stock name... if it is correct add to the watch
# list.
#
watchList = []


def addList(symbol):
    try:
        stockQuote(symbol)
        global watchList
        watchList.append(symbol)

    except ValueError:
        print(symbol + 'is not a correct ticker')


addList('tsla')

print(watchList)
