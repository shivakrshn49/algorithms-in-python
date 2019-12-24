# Sources for ideas 
# 1. https://stackabuse.com/doubly-linked-list-with-python-examples/
# 2. https://www.geeksforgeeks.org/data-structures/linked-list/

class Node(object):
    """
    Node object stores three elememts
    1. Reference to prev node object
    2. data
    3. Reference to next node object
    """
    
    def __init__(self, data):
        # Initial reference to prev node object is None
        self.prev_node_ref = None
        self.data = data
        # Initial reference to next node object is None, because we will handle assinging
        # new node to existing node using another class (Linked list)
        self.next_node_ref = None


class DoubleLinkedList(object):
    """
    Double linked list is data structure that stores the data in the form of 
    node and maintains a reference to both prev and next node(or data) 
    """

    def __init__(self):
        # When a linked list is created, it will be empty and so head
        # will be None/empty
        self.root = None
        # Initially the length of the linked list will be zero,
        # we should increase it for each and every insert, so that
        # we can track the length without traversing the linked list
        self._length = 0
        # Keep track of last element/node
        self.last_node = None 


    def check_if_head_node_exists(self):
        if self.root is None:
            print("No elememts present in the double linked list")
            return

    def insert(self, data, location="end"):
        """
        By default, we will insert data at the end
        """ 

        new_node = Node(data) # Create a new node with data

        # If there is not atleast one element exists, then
        # create a new node and assing it as head node
        if not self.root:
            self.root = self.last_node = new_node
            self._length += 1
            return

        if location == "start":
            # Make the root node as next node of new node
            new_node.next_node_ref = self.root
            self.root.prev_node_ref = new_root_node
            # Increase the length of linked list
            self._length += 1
            # Make the root node as new node
            self.root = new_node
        else:
            # Assing the new node to the last node
            self.last_node.next_node_ref = new_node
            # Assing the last as prev ref to new node 
            new_node.prev_node_ref = self.last_node
            # Make the last node as new node
            self.last_node = new_node
            # Increase the length
            self._length += 1

    def delete(self, location="end"):
        """
        Delete eigther first node or last node
        """
        self.check_if_head_node_exists()
        
        if location == "start":
            # First secure/store the next element/node from the root node
            new_root_node = self.root.next_node_ref
            # Remove the reference from the root node
            self.root.next_node_ref = None
            new_root_node.prev_node_ref = None
            # Assing the new root node
            self.root = new_root_node
            self._length -= 1
        else:
            prev_node = self.last_node.prev_node_ref
            self.last_node.prev_node_ref = None
            prev_node.next_node_ref = None
            self.last_node = prev_node
            current_node = self.root
            self._length -= 1

    def delete_node_with_data(self, data):
        self.check_if_head_node_exists()
        current_node = self.root
        while current_node:
            next_node = current_node.next_node_ref
            prev_node = current_node.prev_node_ref
            if current_node.data == data:
                current_node.prev_node_ref = current_node.next_node_ref = None
                prev_node.next_node_ref = next_node
                next_node.prev_node_ref = prev_node
                self._length -= 1
                break
            current_node = next_node

    def travese_list(self):
        """
        Go through each and every element of the list and print it
        """
        # Check if root / head node exists, if not print "no elements"
        # and return nothing
        self.check_if_head_node_exists()

        # Take inital node as root node
        root_node = self.root
        self.final_list = []
        while root_node:
            # As long as the node exists, print the value of the 
            # node and track/refer the next node
            print(root_node.data)
            self.final_list.append(root_node.data)
            root_node = root_node.next_node_ref

        return self.final_list

    def reverse_linked_list(self):
        # Check if root / head node exists, if not print "no elements"
        # and return nothing
        self.check_if_head_node_exists()
        
        current_node = self.root
        prev = None
        while current_node:
            next_node = current_node.next_node_ref
            current_node.next_node_ref = prev
            prev = current_node
            current_node = next_node
        # Finally make the last element/Node as the head
        self.root = prev

        # Reverse the list and print it
        print(self.travese_list())

    def search(self, data):
        """
        Search whether the element is present in the linked list
        """
        current_node = self.root
        while current_node:
            if current_node.data == data:
                print("Data found")
                return True
            # Assing the next node to the current node
            current_node = current_node.next_node_ref
        # If data found return False
        print("Data not found !!")
        return False

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, data):
        print("You can't set length attribute to linked_list")



linked_list = DoubleLinkedList()

for i in range(1,6):
    # Insert at end of the list
    linked_list.insert(i)

# for i in range(5):
#     # Insert at start of the list
#     linked_list.insert(i, location="start")

print("Length of the linked list after inserting elements is -", linked_list.length, ", And the list is -", linked_list.travese_list())

# print first and last nodes of linked list
# print(linked_list.root.data, linked_list.last_node.data, sep="<====>")

# reverse the linked list
# linked_list.reverse_linked_list()

# Search for an element/data
# print(linked_list.search(3))
# print(linked_list.search(7))

# Delete an element
# linked_list.delete(location="start")
linked_list.delete()
print("After deleting element the list is -", linked_list.travese_list(), ", And the length of the linked list is -", linked_list.length)

# Delete particular node with data
linked_list.delete_node_with_data(2)
print("After deleting particular element the list is -", linked_list.travese_list(), ", And the length of the linked list is -", linked_list.length)