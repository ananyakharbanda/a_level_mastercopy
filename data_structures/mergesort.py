def merge(arr1, arr2):
    merged = []
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append the remaining elements of arr1 (if any)
    while i < n1:
        merged.append(arr1[i])
        i += 1
    
    # Append the remaining elements of arr2 (if any)
    while j < n2:
        merged.append(arr2[j])
        j += 1
    
    return merged


def mergesort(arr, low, high):
    if low == high:
        return [arr[low]]  # Return the subarray as a single-element array
    mid = (low + high) // 2
    left = mergesort(arr, low, mid)  # Sort the left half
    right = mergesort(arr, mid + 1, high)  # Sort the right half
    return merge(left, right)  # Merge the sorted halves


# Test the function
arr = [2, 7, 9, 4, 5, -3]
sorted_arr = mergesort(arr, 0, len(arr) - 1)
print(sorted_arr)


def iterative_mergesort(arr):
    n = len(arr)
    # Initially, subarrays of size 1 are already sorted.
    current_size = 1
    
    # Double the subarray size each time.
    while current_size < n:
        # Start from the left of the array and merge subarrays of size current_size
        for left in range(0, n, 2 * current_size):
            mid = min(left + current_size - 1, n - 1)
            right = min(left + 2 * current_size - 1, n - 1)
            
            if mid < right:  # There are two halves to merge
                left_half = arr[left:mid + 1]
                right_half = arr[mid + 1:right + 1]
                arr[left:right + 1] = merge(left_half, right_half)
        
        current_size *= 2

    return arr


# Testing the iterative merge sort
arr = [2, 7, 9, 4, 5, -3]
sorted_arr = iterative_mergesort(arr)
print(sorted_arr)

