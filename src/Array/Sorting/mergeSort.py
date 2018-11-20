def mergeSort(arr):

    if len(arr) > 1:
        middle = len(arr)//2
        positionLeft = arr[:middle]
        positionRight = arr[middle:]

        mergeSort(positionLeft)
        mergeSort(positionRight)
        i = j = k = 0
        while i < len(positionLeft) and j < len(positionRight):
            if positionLeft[i] < positionRight[j]:
                arr[k] = positionLeft[i]
                i = i+1
            else:
                arr[k] = positionRight[j]
                j = j+1
            k = k+1

        while i < len(positionLeft):
            arr[k] = positionLeft[i]
            i = i+1
            k = k+1

        while j < len(positionRight):
            arr[k] = positionRight[j]
            j = j+1
            k = k+1
