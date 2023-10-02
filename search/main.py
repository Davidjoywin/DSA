from linear_search import linear_search
from binary_search import binary_search

arr = list(range(600000))

linear = linear_search(arr, 500)
print(linear)

binary = binary_search(arr, 560, left=0, right=len(arr))
print(binary)
