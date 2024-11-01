def find_longest_sequences(str):
    dct = {}
    for i in range(len(str)-1):
        if str[i] not in dct:
            dct[str[i]] = [1]
        else:
            if str[i] == str[i-1]:
                dct[str[i]][-1] += 1
            else:
                dct[str[i]].append(1)

    return {k: max(v) for k, v in dct.items()}

# def test_find_longest_sequences():
#     str = 'aaabbccddaabcccccd'
#     assert find_longest_sequences(str) == {'a': 3, 'b': 2, 'c': 5, 'd': 2}
