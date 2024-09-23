
def bubblesort_asc(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print(bubblesort_asc([2,7,9,4,5,-3]))

def bubblesort_desc(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n-i-1):
			if arr[j] < arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print(bubblesort_desc([2,7,9,4,5,-3]))
