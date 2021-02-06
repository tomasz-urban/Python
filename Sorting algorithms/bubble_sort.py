# One way of sorting is bubble sort. Time complexity not too good (O(n^2)) but space complexity O(1)
# This kind of sorting gets first and second item and sorts them, then moves to second and third and sorts them,
# then third and fourth ... and so on. When it gets to the end it starts from beginning until all of them will be sorted

# In the case above there will be 21 comparisons until it gets sorted array.

# Bubble sort is useful only to teach sorting, not efficient

def bubble_sort():
    count = 0
    for i in range(len(num) - 1):
        for j in range(len(num) - i - 1):
            count += 1
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return f'Sorted array: {num}\nNumber of comparisons: {count}'

num = [5, 9, 3, 10, 45, 2, 0]
print(bubble_sort())