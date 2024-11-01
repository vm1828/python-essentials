from balanced_brackets import is_balanced


def test_1():
    assert is_balanced('()') is True


def test_2():
    assert is_balanced(')') is False


def test_3():
    assert is_balanced('(') is False


def test_4():
    assert is_balanced('((()') is False


def test_5():
    assert is_balanced('((()))') is True


def test_6():
    assert is_balanced('([') is False


def test_7():
    assert is_balanced('([])') is True


def test_8():
    assert is_balanced('{{[}}]') is False


def test_9():
    assert is_balanced('{[]{()}}') is True


def test_10():
    assert is_balanced('[{}{})(]') is False
