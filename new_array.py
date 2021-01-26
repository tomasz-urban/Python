# This is an exercise to get familiar with how arrays work
# In here we create our own array with some basic methods just like the built-in array has

class NewArray:
    def __init__(self):
        self.length = 0  # The length of array at the beginning is set to 0
        self.data = {}  # Data in the array is stored as a dictionary with keys (indexes) and values(data)

    def __str__(self):
        return str(self.__dict__)  # This will print attributes of an array in string format

    # First method is "get" - it takes the index of the element and returns this element

    def get(self, index):
        return self.data[index]

    # Second method is "push" - it adds the given item at the end of an array

    def push(self, item):
        self.length += 1  # We extend array ..
        self.data[self.length - 1] = item  # .. and add the item to the end of array

    # Third method is "pop" - which deletes the last item from the array

    def pop(self):
        last_item = self.data[self.length - 1]  # Collecting the last item
        del self.data[self.length - 1]  # Deleting the last item
        self.length -= 1  # Adjusting the length of an array by -1
        return last_item  # Returning deleted element

    # Fourth method is "insert" - it inerts given element with the given index (place in the array)
    # We have to loop through elements, starting at the end of array to given index with the step -1
    # to move elements to the right to make place for given item

    def insert(self, item, index):
        self.length += 1
        for i in range(self.length-1, index, -1):  # Looping through items
            self.data[i] = self.data[i-1]  # Shifting to make place for item
        self.data[index] = item  # adding the item with index

    # Fifth method is "delete" - it deletes element with given index

    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]  # Shifting elements from index to end towards left
        del self.data[self.length - 1]  # Deleting
        self.length -= 1  # Adjusting length


arr = NewArray()
arr.push('a')
arr.push('b')
arr.push(1)
arr.push('c')
arr.push('d')
arr.insert('z', 2)
arr.delete(3)
print(arr)
