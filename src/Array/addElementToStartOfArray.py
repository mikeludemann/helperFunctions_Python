from array import *


def addElementToStartOfArray(arr, newElement):
    newArray = array('i', arr)
    newArray.insert(0, newElement)
    return str(newArray)
