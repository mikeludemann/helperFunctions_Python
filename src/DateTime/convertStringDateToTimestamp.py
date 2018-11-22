import time
import datetime


def convertStringDateToTimestamp(date):
    return time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())
