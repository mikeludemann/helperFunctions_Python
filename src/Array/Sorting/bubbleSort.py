def bubbleSort(arr):
    for position in range(len(arr)-1, 0, -1):
        for i in range(position):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
