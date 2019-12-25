# Below is the Binary Search Tree format
#
#            ______7_______
#           /              \
#        __3__           ___11___
#       /     \         /        \
#      1       5       9         _13
#     / \     / \     / \       /   \
#    0   2   4   6   8   10    12    14


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_node_ref = None
        self.right_node_ref = None

    def __str__(self):
        return self.data

class BinarySearchTree(object):
    def __init__(self):
        # Initially there will be no elements in the tree
        self.root_node = None
        self._all_items = []

    def insert(self, data, current_node=None):
        """
        Insert/Organize the data as per sorted tree structure 
        """
        if current_node is None:
            current_node = self.root_node

        if self.root_node is None:
            self.root_node = Node(data)
        else:
            if data < current_node.data:
                if current_node.left_node_ref is None:
                    current_node.left_node_ref = Node(data)
                else:
                    self.insert(data, current_node.left_node_ref)
            elif data > current_node.data:
                if current_node.right_node_ref is None:
                    current_node.right_node_ref = Node(data)
                else:
                    self.insert(data, current_node.right_node_ref)

    def search(self, data, current_node=None):
        """
        Check whether the element exists in the tree
        """
        if current_node is None:
            current_node = self.root_node

        if data == current_node.data:
            return True
        
        if current_node.left_node_ref:
            self.search(data, current_node.left_node_ref)
        if current_node.right_node_ref:
            self.search(data, current_node.right_node_ref)

        return False

    # def construct_elements(self, current_node=None, items=None):
    #     """
    #     Construct elements of the tree
    #     """
    #     if current_node is None:
    #         current_node = self.root_node

    #     self._all_items.append(current_node.data)

    #     if current_node.left_node_ref:
    #         self.construct_elements(current_node.left_node_ref, self._all_items)

    #     if current_node.right_node_ref:
    #         self.construct_elements(current_node.right_node_ref, self._all_items)
    
    # @property
    # def items(self):
    #     return sorted(self._all_items)


    def items(self, current_node=None, all_items=[]):
        if current_node is None:
            current_node = self.root_node

        all_items.append(current_node.data)

        if current_node.left_node_ref:
            self.items(current_node.left_node_ref, all_items)

        if current_node.right_node_ref:
            self.items(current_node.right_node_ref, all_items)

        return sorted(all_items)

        

bst = BinarySearchTree()
# Insert left side of the tree
bst.insert(10)
bst.insert(5)
bst.insert(3)
bst.insert(1)
bst.insert(12)
# Insert right side of the tree
bst.insert(15)
bst.insert(17)
bst.insert(7)
bst.insert(4)
bst.insert(85)

# bst.construct_elements()
print(bst.items())
print(f"10 exists in list - ", bst.search(10))
