def count_to(count):
    """Iterator implementation"""

    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # built-in iterator, creates a tuple
    iterator = zip(range(count), numbers_in_german)

    # iterate through iterable list
    # put german numbers into a generator
    for position, number in iterator:
        yield number


for num in count_to(3):
    print(num)
