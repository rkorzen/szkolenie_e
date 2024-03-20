from functools import wraps


def dekorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("wywołuję funkcję", func.__name__)
        r = func(*args, **kwargs)
        return r

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__

    return wrapper

def foo():
    print("jestem sobie foo")


@dekorator
def bar():
    """docstring funkcji bar"""
    print("jestem sobie bar")

foo = dekorator(foo)
foo()

bar()

print(help(bar))