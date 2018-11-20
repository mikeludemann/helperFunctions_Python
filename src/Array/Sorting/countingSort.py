def countingSort(arr, maxValue):
    m = maxValue + 1
    count = [0] * m

    for index in arr:
        count[index] += 1
    i = 0

    for index in range(m):
        for c in range(count[index]):
            arr[i] = index
            i += 1

    return arr
