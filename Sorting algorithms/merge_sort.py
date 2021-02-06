# Merge sort (divide and conquer). It breaks up array into half than those halves also in halves and so on
# until there will be only single elements. Then it is merging them in sorted order. Time complexity is O(n log(n))
# space complexity is O(n)

# Very good, every case of time complexity is O(n log(n)). Very fast. Use it always when You are worried about
# worst case (like in quick sort). Only thing is that the space complexity is O(n) so it can be expensive. If we have
# external sorting (not using our work space) this sorting is best.

count = 0

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    left_index = 0
    right_index = 0
    sorted_array = []
    while left_index < 1 and right_index < len(right):
        global count
        count +=1
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    return sorted_array + left[left_index:] + right[right_index:]

array = [5, 9, 3, 10, 45, 2, 0]
print(f'Array: {merge_sort(array)}\nNumber of comparisons: {count}')