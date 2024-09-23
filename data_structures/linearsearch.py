
from mergesort import mergesort, merge

def linear_search_uo(arr, element):
    for i in arr:
        if i == element:
            return True
    return False

def linear_search_o(arr, element):
    for i in arr:
        if i == element:
            return True
        if i > element:
            return False
    return False

arr = [2,7,9,4,5,-3]

print(linear_search_uo(arr, -3))

sorted_arr = mergesort(arr, 0, len(arr)-1)

print(linear_search_o(sorted_arr, 3))