from bubblesort import bubblesort_asc

def binary_rec(arr, element, low, high):
    mid = (low + high) // 2
    if low > high:
        return False
    elif element == arr[mid]:
        return True
    elif element < arr[mid]:
        return binary_rec(arr, element, low, mid-1)
    else:
        return binary_rec(arr, element, mid+1, high)
    

arr = bubblesort_asc([2,7,9,4,5,-3])

print(binary_rec(arr, 44, 0, len(arr)-1))



def binary_ite(arr, element):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if element == arr[mid]:
            return True
        if element > arr[mid]:
            low = mid+1
        else:
            high = mid -1
    return False

print(binary_ite(arr, 44))
