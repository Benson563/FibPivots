# API Key for Alpha Vantage: D1UA2DG18SPT7MCN
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time


key = 'D1UA2DG18SPT7MCN'
ts = TimeSeries(key=key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='MSFT', outputsize='full')
print(data)
print(ts)


