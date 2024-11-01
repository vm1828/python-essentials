from find_longest_sequences import find_longest_sequences

def test_find_longest_sequences():
    str = 'aaabbccddaabcccccd'
    assert find_longest_sequences(str) == {'a': 3, 'b': 2, 'c': 5, 'd': 2}