def binary_search(arr, target, left, right):
    index = (left + right) // 2
    if arr[index] == target:
        return index
    else:
        if arr[index] < target:
            left = index
            return binary_search(arr, target, left, right)
        else:
            right = index
            return binary_search(arr, target, left, right)

