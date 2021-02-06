# Quick sort (divide and conquer). It chooses the pivot and all of the items that are smaller than pivot goes to
# the left, all bigger goes to the right. Pivot stays in this place and we split the rest to two arrays and do the
# same with those arrays.
# Time complexity best case is O(n log(n)), worst O(n^2). Space complexity O(log(n).

# Quick sort is better than merge sort if You are not worried about the worst case of time complexity.
# It has much better space complexity than merge sort. But in most cases it is faster

count = 0


def partition(array, left, right):
    smaller_index = left - 1
    pivot = array[right]  # We can change pivot to pick the middle element or left one, but even if it would
                          # be better with this array it can't guarantee to be better with another one
    for i in range(left, right):
        global count
        count += 1
        if array[i] < pivot:
             smaller_index += 1
             array[smaller_index], array[i] = array[i], array[smaller_index]
    array[smaller_index+1], array[right] = array[right], array[smaller_index+1]
    return smaller_index+1


def quick_sort(array, left, right):
    if left < right:
        partitioning_index = partition(array, left, right)
        quick_sort(array, left, partitioning_index-1)
        quick_sort(array, partitioning_index+1, right)

array = [5, 9, 3, 10, 45, 2, 0]
quick_sort(array, 0, len(array)-1)
print(f'Sorted array: {array}\nNumber of comparisons: {count}')