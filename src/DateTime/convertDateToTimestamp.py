import time
import datetime


def convertDateToTimestamp():
    now = datetime.datetime.now()
    return time.mktime(now.timetuple())
