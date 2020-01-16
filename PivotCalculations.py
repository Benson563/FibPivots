def fibPivot(high , low, close):
    # daily pivots are using MONTHLY high, low, close #4hr-1hr pivots are using weekly high, low, close
    # 15min-1min pivots are using daily high, low, close
    pivotPoint = round(high + low + close) / 3
    r3 = round(pivotPoint + ((high - low) * 1.000), 2)
    r2 = round(pivotPoint + ((high - low) * 0.618), 2)
    r1 = round(pivotPoint + ((high - low) * 0.382), 2)
    s1 = round(pivotPoint - ((high - low) * 0.382), 2)
    s2 = round(pivotPoint - ((high - low) * 0.618), 2)
    s3 = round(pivotPoint - ((high - low) * 1.000), 2)
    pivotList = (r3, r2, r1, pivotPoint, s1, s2, s3)
    return pivotList

