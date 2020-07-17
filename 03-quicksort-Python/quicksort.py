"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	start = array[0]
	end = array[len(array) - 1]
	x = quick_sort(array,start,end)
	return x

def quick_sort(array,start,end):
	if(start >= end):
		return array
	p = partition(array,start,end)
	quick_sort(array,start,p-1)
	quick_sort(array,p+1,end)

def partition(array,start,end):
	pivot = array[start]
	low = start + 1
	high = end
	while True:
		while array[low] >= pivot and low <= high:
			low = low + 1
		while array[high] <= pivot and low <= high:
			high = high - 1
		if(low <= high):
			array[low], array[high] = array[high],array[low]
		else:
			break
	array[start], array[high] = array[high], array[start]
	return high

print(quick_sort([3,5,1,89,98,54,4],0,6))
	