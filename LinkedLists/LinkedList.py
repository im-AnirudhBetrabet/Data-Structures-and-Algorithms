from LinkedLists.Node import Node


class LinkedList:
    def __init__(self):
        self.head   = None
        self.tail   = None
        self.length = 0

    """
    The append method is used to add a new node with the specified value to the end of the linked list.
    Time Complexity: O(n) - In the worst case, we may need to traverse the entire list to find the last node,
    where n is the number of nodes in the list.
    
    """
    def append(self, value) -> bool:
        new_node : Node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node
        self.length += 1
        return True