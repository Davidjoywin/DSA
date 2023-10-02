def bubble_sort(arr):
    for _ in arr:
        for indx in range(len(arr)-1):
            if arr[indx] > arr[indx+1]:
                arr[indx], arr[indx+1] = arr[indx+1], arr[indx]
    return arr

import random

arr = random.sample(range(1000), 500)
print(arr)
print(bubble_sort(arr))
