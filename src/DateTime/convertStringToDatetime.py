from datetime import datetime


def convertStringToDatetime(dt):
    return datetime.strptime(dt, '%b %d %Y %I:%M%p')
