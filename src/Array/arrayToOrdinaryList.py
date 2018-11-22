from array import *


def arrayToOrdinaryList(arr):
    newArray = array('i', arr)
    newList = newArray.tolist()
    return str(newList)
