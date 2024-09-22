def partition(arr, low, high):
    pivot = arr[low]
    leftm = low + 1
    rightm = high
    done = False
    while not done:
        while leftm <= rightm and arr[leftm] <= pivot:
            leftm += 1
        while rightm >= leftm and arr[rightm] > pivot:
            rightm -= 1
        if leftm > rightm:
            done = True
        else:
            arr[leftm], arr[rightm] = arr[rightm], arr[leftm]
    arr[low], arr[rightm] = arr[rightm], arr[low]
    return rightm

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)
    return arr

# Testing the function
arr = [2, 7, 9, 4, 5, -3]
# print(quicksort(arr, 0, len(arr) - 1))


def quicksort_iterative(arr, low, high):
    stack = []
    stack.append((low, high))
    
    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high)
            stack.append((low, p - 1))
            stack.append((p + 1, high))
    return arr

arr = [2, 7, 9, 4, 5, -3]
print(quicksort_iterative(arr, 0, len(arr) - 1))