# API Key for Alpha Vantage: D1UA2DG18SPT7MCN
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

key = 'D1UA2DG18SPT7MCN'


def dailyPivotInfo(symbol):  # gotta figure out how to parse of the daily info..
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    print(data.head(1))  # gives off the data of the last trading day


def weeklyPivotInfo(symbol):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_weekly(symbol=symbol)
    print(data.head(1)) #gets the last weeks trading info


def stockQuote(symbol):  # still gotta figure out how to parse
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_quote_endpoint(symbol=symbol)
    print(data)
