from palindrome_checker_deque import is_palindrome
from pytest import mark


@mark.parametrize('test_input,expected', [
    ('aba', True), ('a', False), ('ab', False), ('madam', True), ('refer', True), (111, False)])
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
