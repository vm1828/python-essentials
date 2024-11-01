import pytest
from palindrome_checker import is_palindrome, remove_punctuation


@pytest.mark.parametrize('test_string, expected', [
    ("I'm a string, but with no punctuation!!", 'Imastringbutwithnopunctuation')
])
def test_remove_punctuation(test_string, expected):
    assert remove_punctuation(test_string) == expected


@pytest.mark.parametrize('test_string, expected', [
    ('not a palindrome', False),
    ('Was it a cat I saw?', True),
    ("Madam I'm Adam", True),
])
def test_is_palindrome(test_string, expected):
    assert is_palindrome(test_string) == expected
