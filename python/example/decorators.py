import datetime
from functools import wraps


def my_decorator(f):
    @wraps(f)
    # works below
    # def wrapper(message, *args, **kwds):
    #     print('Calling decorated function: %s' % message)
    #     return f(message, *args, **kwds)
    def wrapper(*args, **kwds):
        message = args[0]
        print('Calling decorated function: %s' % message)
        return f(message, **kwds)
    return wrapper


@my_decorator
def example(message):
    """Docstring"""
    print('Called example function: %s' % message)


def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family


def auto_load_time(func):

    @wraps(func)
    def func_wrapper(hour):
        if isinstance(hour, datetime.time):
            return func(hour)
        assert isinstance(hour, int)
        return func(datetime.time(hour))

    return func_wrapper


@auto_load_time
def print_time(t):
    assert isinstance(t, datetime.time)
    print(t)


if __name__ == '__main__':
    # example('Hello, world')

    # my_person = Person()
    # print(my_person.get_fullname())

    # print(get_text.__name__) # get_text
    # print(get_text.__doc__) # returns some text
    # print(get_text.__module__) # __main__

    print(print_time.__name__)
    print_time(datetime.time(1))
    print_time(4)
