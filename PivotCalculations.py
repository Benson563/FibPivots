def fibPivot(high, low, close):
    # daily pivots are using MONTHLY high, low, close #4hr-1hr pivots are using weekly high, low, close
    # 15min-1min pivots are using daily high, low, close
    pivotPoint = (high + low + close) / 3
    r3 = pivotPoint + ((high - low) * 1.000)
    r2 = pivotPoint + ((high - low) * 0.618)
    r1 = pivotPoint + ((high - low) * 0.382)
    s1 = pivotPoint - ((high - low) * 0.382)
    s2 = pivotPoint - ((high - low) * 0.618)
    s3 = pivotPoint - ((high - low) * 1.000)



