# channel 10tDolCmWafcaCWG.


##Know the pivot points.. Now work on the timing of when this should be running.
## every minute.. call api for current price --- save that current price --- when called the next minute ---
## -- check if passed ANY (Monthly Piv, Daily, Intra) pivot points --- notify if passed -- then save curr price
## if not passed -- no notify --- save curr price
import PivotCalculations
import API
from datetime import datetime
import time
def weekday():
    weekdays = [0, 1, 2, 3, 4]
    today = datetime.today().weekday()
    for days in weekdays:
        if today != days:
            pass
        else:
            return True
    return False

def timeInterval():

    currTime = str(time.ctime()).split(' ')[3].split(':')
    hour = currTime[0]
    minutes = currTime[1]
    if (int(hour) >= 8) & (int(hour) < 15):
        if int(hour) == 8 & int(minutes) < 30:
            return False
        else:
            return True

    print('false')

def callAPI():
    if(timeInterval() == True) & (weekday() == True):
        #CALLL API
        pivotPoints = API.dailyPivotInfo('tsla')
        currQuote = API.stockQuote('tsla')
        for pivot in pivotPoints:
            if currQuote != pivot:

                print(' fjkl')


if __name__ == '__main__':
    while True:
        callAPI()
        print('YO')
        time.sleep(60)
        print('YOYO')
def test():
    print('test 1')
    T = time.sleep(5)
    print('test 2')

test()