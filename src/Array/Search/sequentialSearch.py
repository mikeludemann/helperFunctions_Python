def sequentialSearch(arr, searchElement):

    position = 0
    found = False

    while position < len(arr) and not found:
        if arr[position] == searchElement:
            found = True
        else:
            position = position + 1

    return found
