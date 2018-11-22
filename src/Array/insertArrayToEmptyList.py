from array import *


def insertArrayToEmptyList(arr):
    arrFirst = array('i', [])
    arrFirst.fromlist(arr)
    return str(arrFirst)
