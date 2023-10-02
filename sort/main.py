import random
from bubble_sort import bubble_sort

arr = random.sample(range(50000), 5000)
print(f"Unsorted array: {arr}")

print("\n")

sorted_arr = bubble_sort(arr)
print(f"Sorted array {sorted_arr}")
