def insertionSort(arr):

    for index in range(1, len(arr)):

        currentPosition = arr[index]
        position = index

        while position > 0 and arr[position-1] > currentPosition:
            arr[position] = arr[position-1]
            position = position-1

        arr[position] = currentPosition
