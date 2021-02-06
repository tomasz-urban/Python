#Selection sort is not very useful. It is not efficient. Time complexity O(n^2) in all of the cases.

# Scanning list of items looking for smallest one and switches with the first item. Doing this again and again.

def selection_sort():
    count = 0
    for i in range(len(num)-1):
        min = num[i]
        min_index = i
        for j in range(i+1, len(num)):
            count += 1
            if num[j] < min:
                min = num[j]
                min_index = j
        if min_index != i:
            num[min_index], num[i] = num[i], num[min_index]
    return f'{num}\nNumber of comparisons: {count}'


num = [5, 9, 3, 10, 45, 2, 0]
print(selection_sort())