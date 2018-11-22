from array import *


def reverseArray(arr):
    newArray = array('i', arr)
    newArray.reverse()
    return str(newArray)
