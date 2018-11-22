from array import *


def removeElementFromArray(arr, position):
    newArray = array('i', arr)
    newArray.position(position)
    return str(newArray)
