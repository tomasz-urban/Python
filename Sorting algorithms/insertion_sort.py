#Insertion sort is the method of sorting where we start from second element, compare it to the first one and sort it,
#then we take third element and put it in the right spot within those 3 elements (it can be at the beginning, end or
#in the middle. We do the same with all the other elements.
# [6, 5, 3, 1, 4, 2]
# [5, 6, 3, 1, 4, 2] - first comparison
# [3, 5, 6, 1, 4, 2] - second and so on..
# [1, 3, 5, 6, 4, 2]
# [1, 3, 4, 5, 6, 2]
# [1, 2, 3, 4, 5, 6]

#Insertion sort should be used with only a few items (small input), mostly sorted

# def insertion_sort():
#     count = 0
#     for i in range(1, len(num)):
#         last = num[i-1]
#         count += 1
#         if num[i] < last:
#             temp = num[i]
#             for j in range(i-1, -1, -1):
#                 count += 1
#                 if temp < num[j]:
#                     if j == 0:
#                         num[j+1] = num[j]
#                         num[j] = temp
#                     else:
#                         num[j+1] = temp
#                         break
#     return f'{num}\nNumber of comparisons: {count}'
#
#
# num = [5, 9, 3, 10, 45, 2, 0]
# print(insertion_sort())

def insertion_sort():
    i = 1
    end = num[0]
    while i < len(num):
        if num[i] < end:
            temp = num.pop(i)
            for j in range(0, i):
                if temp < num[j]:
                    num.insert(j, temp)
                    break
        end = num[i]
        i += 1
    return num

num = [5, 9, 3, 10, 45, 2, 0]
print(insertion_sort())
