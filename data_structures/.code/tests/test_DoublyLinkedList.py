import pytest
from DoublyLinkedList import Node, LinkedList


# test Node class

@pytest.fixture()
def node1():
    yield Node('apple')


@pytest.fixture()
def node2():
    yield Node(1234)


def test_Node_get_data(node1):
    assert node1.get_data() == 'apple'


def test_Node_set_data(node1):
    node1.set_data('pear')
    assert node1.get_data() == 'pear'


def test_Node_get_next(node1, node2):
    assert node1.get_next() is None
    node1.set_next(node2)
    assert node1.get_next() == node2
    assert node2.get_next() is None


def test_Node_get_previous(node1, node2):
    assert node2.get_previous() is None
    node2.set_previous(node1)
    assert node2.get_previous() == node1
    # assert node1.get_next() == node2


def test_Node_repr(node2):
    print(node2)
    assert repr(node2) == "<Node object: data=1234>"


# test LinkedList class

@pytest.fixture()
def l_list():
    yield LinkedList()


def test_LinkedList_repr(l_list):
    assert repr(l_list) == "<LinkedList object: head=None>"


def test_LinkedList_is_empty(l_list, node1):
    assert l_list.is_empty() is True
    l_list.head = node1
    assert l_list.is_empty() is False


def test_LinkedList_add_front(l_list):
    assert l_list.is_empty() is True
    assert l_list.head is None
    l_list.add_front(2345)
    assert l_list.is_empty() is False
    assert l_list.head.get_data() == 2345
    # l_list.head is not None now, the head is pointing at the Node we added
    assert l_list.head.get_next() is None
    assert l_list.head.get_previous() is None

    # add another node
    l_list.add_front(1234)
    assert l_list.head.get_data() == 1234
    assert l_list.head.get_previous() is None
    assert l_list.head.get_next().get_data() == 2345
    assert l_list.head.get_next().get_previous().get_data() == 1234


def test_LinkedList_size(l_list):
    assert l_list.size() == 0
    l_list.add_front(1234)
    assert l_list.size() == 1
    l_list.add_front(2345)
    assert l_list.size() == 2


def test_LinkedList_search(l_list):
    assert l_list.search(1234) == "LinkedList is empty. No Nodes to search"
    l_list.add_front(1234)
    l_list.add_front(2345)
    assert l_list.search(1234) is True
    assert l_list.search('asdf') is False


def test_LinkedList_remove_from_empty_list(l_list):
    assert l_list.remove(1234) == "LinkedList is empty. No Nodes to remove."


def test_LinkedList_remove_single_node(l_list):
    assert l_list.head is None
    l_list.add_front(1234)
    assert l_list.head.get_data() == 1234
    assert l_list.remove(2345) == "A Node with that data value is not present."
    l_list.remove(1234)
    assert l_list.head is None


def test_LinkedList_remove_first_node(l_list):
    l_list.add_front(2345)
    l_list.add_front(1234)
    assert l_list.size() == 2
    assert l_list.head.get_data() == 1234
    assert l_list.head.get_next().get_data() == 2345
    assert l_list.head.get_previous() is None
    assert l_list.head.get_next().get_next() is None
    assert l_list.head.get_next().get_previous().get_data() == 1234

    l_list.remove(1234)
    assert l_list.size() == 1
    assert l_list.head.get_data() == 2345
    assert l_list.head.get_next() is None
    assert l_list.head.get_previous() is None


def test_LinkedList_remove_node(l_list):
    l_list.add_front(3456)
    l_list.add_front(2345)
    l_list.add_front(1234)
    assert l_list.size() == 3

    node1 = l_list.head
    node2 = node1.get_next()
    node3 = node2.get_next()

    assert node2.get_previous() == node1
    assert node3.get_previous() == node2

    l_list.remove(2345)

    assert l_list.size() == 2
    assert node1.get_data() == 1234
    assert node3.get_data() == 3456
    assert node1.get_next() == node3
    assert node3.get_previous() == node1
