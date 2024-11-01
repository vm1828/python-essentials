class Stack:
    # The Stack class is built on top of python list

    def __init__(self):
        self.items = []

    def push(self, item):
        """Acceptes an item as a parameter and adds it to the stack.
        Returns nothing.
        The time complexity is O(1) (constant time).
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item of the Stack.
        Returns None if stack is empty.
        The runtime is constant - O(1).
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns top item of the Stack.
        Returns None if stack is empty.
        The runtime is constant - O(1).
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list that is representing the Stack.
        The runtime is constant - O(1).
        """
        return len(self.items)

    def is_empty(self):
        """Returns the boolean value describing whether the stack is empty.
        Testing for equality happens in constant time.
        """
        return self.items == []
