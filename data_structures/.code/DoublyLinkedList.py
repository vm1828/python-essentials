# Doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"<Node object: data={self.data}>"

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"<LinkedList object: head={self.head}>"

    def is_empty(self):
        """Returns True if the LinkedList is empty. Otherwise, returns False."""
        return self.head is None

    def add_front(self, new_data):
        """Add a Node whose data is  the new_data argument to the front of the LinkedList"""
        new_node = Node(new_data)
        new_node.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(new_node)  # self.head is still an old node
        self.head = new_node

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument as its self.data variable.
        The time complexity is O(n).
        """
        if self.head is None:
            return "LinkedList is empty. No Nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
            if self.head is not None:
                # in the case of LinkedList with single Node we can't access 'set_previous' attribute from NoneType object
                self.head.set_previous(None)
        else:
            current.get_previous().set_next(current.get_next())
            current.get_next().set_previous(current.get_previous())

    def size(self):
        """Traverses the LinkedList and returns an integer value representing the number of nodes in the LinkedList.
        The time complexity is O(n).
        """
        size = 0
        current = self.head
        while current is not None:  # while there are still Nodes left to count
            size += 1
            current = current.get_next()
        return size

    def search(self, data):
        """Traverses the LinkedList and returns True if the data searched for is present in one of the Nodes.
        Otherwise, it returns False.
        The time complexity is O(n).
        """
        if self.head is None:
            return "LinkedList is empty. No Nodes to search"
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False
