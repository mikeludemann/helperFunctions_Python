from array import *


def addElementToEndOfArray(arr, newElement):
    newArray = array('i', arr)
    newArray.append(newElement)
    return str(newArray)
