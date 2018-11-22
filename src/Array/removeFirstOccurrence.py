from array import *


def removeFirstOccurrence(arr, element):
    newArray = array('i', arr)
    newArray.remove(element)
    return str(newArray)
