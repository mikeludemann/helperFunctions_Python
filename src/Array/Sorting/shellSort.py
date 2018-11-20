def shellSort(arr):
    counter = len(arr)//2
    while counter > 0:
        for startPosition in range(counter):
            swapInsertionSort(arr, startPosition, counter)

        counter = counter // 2


def swapInsertionSort(arr, start, index):
    for i in range(start+index, len(arr), index):

        currentPosition = arr[i]
        position = i

        while position >= index and arr[position-index] > currentPosition:
            arr[position] = arr[position-index]
            position = position-index

        arr[position] = currentPosition
