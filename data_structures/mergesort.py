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


def merge_ite(arr, left, mid, right):
    # Create temporary subarrays
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Merge the subarrays
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of left_part, if any
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of right_part, if any
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def iterative_mergesort(arr):
    n = len(arr)
    curr_size = 1  # Start with subarrays of size 1
    
    # Merge subarrays in bottom-up manner
    while curr_size < n:
        left = 0
        # Pick the starting point of different subarrays of current size
        while left < n - 1:
            mid = min((left + curr_size - 1), (n - 1))  # Calculate the mid index
            right = min((left + 2 * curr_size - 1), (n - 1))  # Calculate the right index
            
            # Merge subarrays arr[left...mid] and arr[mid+1...right]
            merge_ite(arr, left, mid, right)
            
            left += 2 * curr_size
        
        # Double the subarray size
        curr_size *= 2
    
    return arr

# Testing the iterative merge sort
arr = [2, 7, 9, 4, 5, -3]
sorted_arr = iterative_mergesort(arr)
print(sorted_arr)

