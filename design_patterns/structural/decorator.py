from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # this makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # define the inner function
    def decorator():
        # grab the return value of the function being decorated
        ret = function()
        # add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator

# apply the decorator


@make_blink
def hello_world():
    """Original function"""
    return "Hello world!"


# check the results of decorating
print(hello_world())

# check if the function name and docstring are still the same as the original function being decorated
print(hello_world.__name__)
print(hello_world.__doc__)
