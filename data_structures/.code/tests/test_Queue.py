import pytest
from Queue import Queue
import pytest


@pytest.fixture()
def queue():
    queue = Queue()
    queue.enqueue('apple')
    queue.enqueue('pear')
    queue.enqueue('banana')
    yield queue


def test_Queue_enqueue(queue):
    assert queue.items == ['banana', 'pear', 'apple']
    assert queue.items[0] == 'banana'
    queue.enqueue('carrot')
    assert queue.items[0] == 'carrot'
    assert len(queue.items) == 4
    assert Queue().items == []


def test_Queueu_dequeue_from_empty_queue():
    queue = Queue()
    assert queue.dequeue() is None


def test_Queue_dequeue(queue):
    assert queue.items == ['banana', 'pear', 'apple']
    assert queue.dequeue() == 'apple'
    assert queue.items == ['banana', 'pear']
    assert queue.dequeue() == 'pear'
    assert queue.dequeue() == 'banana'
    assert queue.items == []


def test_Queue_peek_from_empty_queue():
    queue = Queue()
    assert queue.peek() is None


def test_Queue_peek(queue):
    """Shows the first item in the queue, which can be dequeued"""
    assert queue.peek() == 'apple'
    queue.dequeue()
    assert queue.peek() == 'pear'


def test_Queue_size(queue):
    assert queue.size() == 3
    queue.dequeue()
    assert queue.size() == 2
    assert Queue().size() == 0


def test_queue_is_empty(queue):
    assert queue.is_empty() is False
    assert Queue().is_empty() is True
