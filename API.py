# API Key for Alpha Vantage: D1UA2DG18SPT7MCN
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time


def dailyPivotInfo(): #gotta figure out how to parse of the daily info..
    key = 'D1UA2DG18SPT7MCN'
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol='MSFT', outputsize='full')
    print((data.head(1))) #gives off the data of the last trading day



def intradayInfo():
