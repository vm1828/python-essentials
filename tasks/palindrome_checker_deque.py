class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)


def is_palindrome(s):
    if not isinstance(s, str) or len(s) < 2:
        return False
    deque = Deque()
    for char in s:
        deque.add_rear(char)
    while deque.size() >= 2:
        front_item = deque.remove_front()
        rear_item = deque.remove_rear()
        if front_item != rear_item:
            return False
    return True
