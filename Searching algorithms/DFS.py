# DFS - depth first search
# As the name suggests we have to go as deep as we can in the tree(graph) and if we hit the end we go back and repeat
# this step for others (not visited) nodes

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

# We have 3 types of DFS: Preorder, Inorder, Postorder
    def DFS_Inorder(self):
        return inorder_traversal(self.root, [])

    def DFS_Preorder(self):
        return preorder_traversal(self.root, [])

    def DFS_Postorder(self):
        return postorder_traversal(self.root, [])

def inorder_traversal(node, DFS_list):
    if node.left:
        inorder_traversal(node.left, DFS_list)
    DFS_list.append(node.data)
    if node.right:
        inorder_traversal(node.right, DFS_list)
    return DFS_list

def preorder_traversal(node, DFS_list):
    DFS_list.append(node.data)
    if node.left:
        preorder_traversal(node.left, DFS_list)
    if node.right:
        preorder_traversal(node.right, DFS_list)
    return DFS_list

def postorder_traversal(node, DFS_list):
    if node.left:
        postorder_traversal(node.left, DFS_list)
    if node.right:
        postorder_traversal(node.right, DFS_list)
    DFS_list.append(node.data)
    return DFS_list

my_bst = BST()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)

print(my_bst.DFS_Inorder())
##[0, 1, 3, 5, 7, 10, 13, 65]

# print(my_bst.DFS_Preorder())
## [5, 3, 1, 0, 7, 13, 10, 65]

# print(my_bst.DFS_Postorder())
##[0, 1, 3, 10, 65, 13, 7, 5]