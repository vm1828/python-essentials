from Stack import Stack
import pytest


@pytest.fixture()
def stack():
    stack = Stack()
    stack.push('apple')
    stack.push('pear')
    stack.push('banana')
    # stack.items == ['apple', 'pear', 'banana', ]
    yield stack


def test_Stack_push():
    stack = Stack()
    assert stack.items == []
    stack.push('apple')
    assert stack.items == ['apple', ]
    stack.push('pear')
    assert stack.items == ['apple', 'pear', ]


def test_Stack_pop_from_empty_stack():
    stack = Stack()
    assert stack.pop() is None


def test_Stack_pop(stack):
    item = stack.pop()
    assert item == 'banana'
    assert stack.items == ['apple', 'pear', ]


def test_Stack_peek_from_empty_stack():
    stack = Stack()
    assert stack.peek() is None


def test_Stack_peek(stack):
    """Shows the value that is on the top of the stack and can be popped"""
    assert stack.peek() == 'banana'
    stack.pop()
    assert stack.peek() == 'pear'


def test_Stack_size(stack):
    assert stack.size() == 3
    stack.pop()
    assert stack.size() == 2
    assert Stack().size() == 0


def test_Stack_is_empty(stack):
    assert stack.is_empty() is False
    assert Stack().is_empty() is True
