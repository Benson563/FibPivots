# API Key for Alpha Vantage: D1UA2DG18SPT7MCN
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

key = 'D1UA2DG18SPT7MCN'


def dailyPivotInfo(symbol):  # gotta figure out how to parse of the daily info..
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    high = data.iloc[0,1]  # ['1. open', '2. high', '3. low', '4. close', '5. volume']
    low = data.iloc[0,2]
    close = data.iloc[0,3]






def weeklyPivotInfo(symbol):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_weekly(symbol=symbol)
    print(data.head(1))  # gets the last weeks trading info


def monthlyPivotInfo(symbol):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_monthly(symbol=symbol)
    print(data.head(1))


def stockQuote(symbol):  # still gotta figure out how to parse
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_quote_endpoint(symbol=symbol)
    print(data)
