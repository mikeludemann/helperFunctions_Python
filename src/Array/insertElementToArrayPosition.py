from array import *


def insertElementToArrayPosition(arr, newElement, position):
    newArray = array('i', arr)
    newArray.insert(position, newElement)
    return str(newArray)
