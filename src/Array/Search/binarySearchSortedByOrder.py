def binarySearchSortedByOrder(arrOrder, searchElement):

    if len(arrOrder) == 0:
        return False
    else:
        middle = len(arrOrder) // 2
        if arrOrder[middle] == searchElement:
            return True
        else:
            if searchElement < arrOrder[middle]:
                return binarySearch(arrOrder[:middle], searchElement)
            else:
                return binarySearch(arrOrder[middle+1:], searchElement)


def binarySearch(arr, searchElement):

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if arr[middle] == searchElement:
            found = True
        else:
            if searchElement < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return found
