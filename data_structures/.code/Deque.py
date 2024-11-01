class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Add an item to the front of the deque.
        The runtime is linear O(n).
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear of the deque.
        The runtime is constant O(1).
        """
        self.items.append(item)

    def remove_front(self):
        """Removes and returns an item from the front of the deque or returns None if the deque is empty.
        The runtime is linear O(n).
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """Removes and returns an item from the rear of the deque or returns None if the deque is empty.
        The runtime is constant O(1).
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """Returns an item from the front of the deque or None if the deque is empty.
        The runtime is constant O(1).
        """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """Returns an item from the rear of the deque or None if the deque is empty.
        The runtime is constant O(1).
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the deque.
        The runtime is constant (because python list object keeps track of its length).
        """
        return len(self.items)

    def is_empty(self):
        """Check if the deque is empty.
        The runtime is constant O(1).
        """
        return self.items == []
