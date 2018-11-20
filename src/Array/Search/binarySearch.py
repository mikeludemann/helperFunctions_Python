def binarySearch(arr, searchElement):

    first = 0
    last = len(arr)-1
    found = False

    while(first <= last and not found):
        middle = (first + last)//2
        if arr[middle] == searchElement:
            found = True
        else:
            if searchElement < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return found
