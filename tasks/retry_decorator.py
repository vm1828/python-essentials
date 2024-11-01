def retry_decorator(f):
    def wrapper(*args):
        for n in range(1, 4):
            try:
                result = f(*args)
                print(f'Function called without exception\n')
                return result
            except Exception as e:
                print(f'Retry nubmer {n}')
                print(
                    f'Function execution with arguments {args} failed with exception:\n {e}.\n')
                n += 1
        print(f'Retry number exceeded. Quit function execution...\n')
    return wrapper


@retry_decorator
def error_function(a, b):
    print('error_function called')
    return a*b


if __name__ == '__main__':
    error_function('asdf', 'sdfg')
    # error_function(3, 5)
