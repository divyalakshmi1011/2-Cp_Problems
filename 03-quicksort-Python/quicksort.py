"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	start = 0
	end = len(array) - 1
	quick_sort(array,start,end)
	return array

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


def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
	

print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))