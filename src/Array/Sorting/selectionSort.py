def selectionSort(arr):
    for firstPosition in range(len(arr)-1, 0, -1):
        maxPosition = 0
        for position in range(1, firstPosition+1):
            if arr[position] > arr[maxPosition]:
                maxPosition = position

        temp = arr[firstPosition]
        arr[firstPosition] = arr[maxPosition]
        arr[maxPosition] = temp
