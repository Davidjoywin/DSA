def linear_search(arr, target):
    for indx in arr:
        if arr[indx] == target:
            return indx
    return -1

