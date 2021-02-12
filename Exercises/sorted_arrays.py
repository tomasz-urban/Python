# Create a function that will merge two sorted arrays in one also sorted array

def merge_sorted_arrays(array1, array2):
    # First we have to take care of an example where there is an empty array
    if not array1 or not array2:
        return array2 + array2
    # If we have two arrays, we start looping through arrays starting from index 0 to the end
    i = 0
    j = 0
    new_array = []
    while i < len(array1) and j < len(array2):
        # We are looking for lowest number in both arrays to start from that one
        if array1[i] <= array2[j]:
            new_array.append(array1[i])
            i += 1
        elif array2[j] < array1[i]:
            new_array.append(array2[j])
            j += 1
    # We return appended array together with what's left from the array that was longer
    # One of them is empty so we are adding both because we don't know which one is that
    return new_array+array1[i:]+array2[j:]


merged = merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
print(merged)


# An easy way to do this:

# def merge_sorted_arrays(array1, array2):
#     merged_array = sorted(array1 + array2)
#     return merged_array
#
# merged = merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
# print(merged)
