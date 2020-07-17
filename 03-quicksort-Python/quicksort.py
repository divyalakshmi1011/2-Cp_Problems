"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	start = 0
	end = len(array) - 1
	if start >= end:
		return
		p = partition(array, start, end)
		quicksort(array, start, p-1)
		quicksort(array, p+1, end)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

	
array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

quicksort(array)
print(array)