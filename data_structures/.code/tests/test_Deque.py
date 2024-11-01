from pytest import fixture
from Deque import Deque


@fixture()
def deque():
    deque = Deque()
    deque.items = ['apple']
    yield deque


def test_Deque(deque):
    assert Deque().is_empty() is True
    assert Deque().size() == 0

    assert deque.is_empty() is False
    assert deque.size() == 1

    assert deque.items == ['apple']
    deque.add_front('front')
    assert deque.items == ['front', 'apple']
    deque.add_rear('rear')
    assert deque.items == ['front', 'apple', 'rear']

    assert deque.size() == 3

    assert deque.peek_front() == 'front'
    assert deque.peek_rear() == 'rear'

    deque.remove_front()
    assert deque.items == ['apple', 'rear']
    deque.remove_rear()
    assert deque.items == ['apple']
