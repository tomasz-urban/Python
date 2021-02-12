# BFS - breadth first search
# We start from the root node and check all the levels from left to right.
# We keep track of all the children we visit so if we get to next level
# we kno which node to visit next

# First we need to implement BST - binary search tree
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.number_of_nodes += 1
            return


    def search(self, data):
        if self.root == None:
            return "Empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return "Not found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right


    def remove(self, data):
        if self.root == None:
            return "Empty"
        current_node = self.root
        parent_node = None
        while current_node != None:
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return
                # Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                # No right and no left child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None:
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                # Node has right and left child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None:
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data
                    if del_node == del_node_parent:
                        current_node.right = del_node.right
                        return
                    if del_node.right == None:
                        del_node_parent.left = None
                        return
                    else:
                        del_node_parent.left = del_node.right
                        return
        return "Not found"

# Now we can implement BFS method
# We start from the root node, store result in an array and use queue to keep track of children of each node

    def BFS(self):
        current_node = self.root
        BFS_result = []
        queue = []
        queue.append(current_node) # We add the root node as a first element
        while len(queue) > 0:
            current_node = queue.pop(0) # Take the first element to be current node
            BFS_result.append(current_node.data) # Add data of the current node to the results
            if current_node.left:
                queue.append(current_node.left) # If left child exists - add it to queue
            if current_node.right:
                queue.append(current_node.right) # If right child exists - add it to queue
        return BFS_result

# We can also use recursive version of BFS method

    def BFS_recursive(self, queue, BFS_list):
        if len(queue) == 0:
            return BFS_list
        current_node = queue.pop(0)
        BFS_list.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.BFS_recursive(queue, BFS_list)



my_bst = BST()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)


# print(my_bst.BFS())

# With recursive version we have to pass root node as an array and empty array to get results
print(my_bst.Recursive_BFS([my_bst.root],[]))