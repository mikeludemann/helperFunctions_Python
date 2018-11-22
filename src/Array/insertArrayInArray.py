from array import *


def insertArrayToArray(firstArray, secondArray):
    arrFirst = array('i', firstArray)
    arrSecond = array('i', secondArray)
    arrFirst.extend(arrSecond)
    return str(arrFirst)
