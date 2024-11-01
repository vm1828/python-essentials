import re


def remove_punctuation(s):
    return re.sub(r'\W+', '', s)


def is_palindrome(s):
    s = remove_punctuation(s).lower()
    return s == s[::-1]
