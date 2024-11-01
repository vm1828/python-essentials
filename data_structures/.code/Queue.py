class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Inserts the item into the index 0 of the list.
        The runtime is linear - O(n).
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Removes and returns the first item in the Queue.
        Returns None if Queue is empty.
        The runtime is constant - O(1).
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns first item in the Queue.
        Returns None if queue is empty.
        The runtime is constant - O(1).
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list that is representing the Queue.
        The runtime is constant - O(1).
        """
        return len(self.items)

    def is_empty(self):
        """Returns the boolean value describing whether the queue is empty.
        Testing for equality happens in constant time.
        """
        return self.items == []
