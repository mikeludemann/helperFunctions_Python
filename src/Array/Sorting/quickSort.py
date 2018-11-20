def quickSort(arr):
    swapQuickSort(arr, 0, len(arr)-1)


def swapQuickSort(arr, first, last):
    if first < last:

        splitter = partition(arr, first, last)

        swapQuickSort(arr, first, splitter-1)
        swapQuickSort(arr, splitter+1, last)


def partition(arr, first, last):

    pivotvalue = arr[first]

    positionLeft = first+1
    positionRight = last

    done = False
    while not done:

        while positionLeft <= positionRight and arr[positionLeft] <= pivotvalue:
            positionLeft = positionLeft + 1

        while arr[positionRight] >= pivotvalue and positionRight >= positionLeft:
            positionRight = positionRight - 1

        if positionRight < positionLeft:
            done = True
        else:
            temp = arr[positionLeft]
            arr[positionLeft] = arr[positionRight]
            arr[positionRight] = temp

    temp = arr[first]
    arr[first] = arr[positionRight]
    arr[positionRight] = temp

    return positionRight
