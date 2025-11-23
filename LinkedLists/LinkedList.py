from Node import Node
from typing import Optional

class LinkedList:
    def __init__(self):
        self.head   = None
        self.tail   = None
        self.length = 0

    # Over-riding len function to retrieve the length of the linked list
    def __len__(self):
        return self.length

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

    """
    The pop method is used to remove the last node from the linked list and return it.
    Time Complexity: O(n) - In the worst case, we may need to traverse the entire list to find the second-to-last node,
    where n is the number of nodes in the list.
    """
    def pop(self) -> Optional[Node]:
        # Edge case scenario where the linked list is empty
        if self.length == 0:
            return None

        current_node  : Node = self.head
        previous_node : Node = self.head

        # Traverse to the second to last node
        while current_node.next:
            previous_node = current_node
            current_node  = current_node.next

        # Update the tail
        self.tail      = previous_node
        self.tail.next = None
        self.length   -= 1

        # If the list became empty
        if self.length == 0:
            self.head = None
            self.tail = None

        return current_node

    """
    The prepend method is used to add a new node to the beginning of the linked list.
    Time Complexity: O(1) - Even in the worst case scenario, the prepend operation can be completed in constant time we always have access to the head.
    """
    def prepend(self, value) -> int:
        new_node : Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return self.length