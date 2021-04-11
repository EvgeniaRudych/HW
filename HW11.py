from functools import wraps


# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    def inner_func(a, b):
        return func(a, b) * 2

    return inner_func


def add(a, b):
    return a + b


print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20
print(add(20, 60))  # 160


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd(нечетные) numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    def inner_func(*args):
        for a in args:
            if a % 2 == 0:
                return f"Please use only odd numbers!"
        return func(*args)

    return inner_func


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    @wraps(func)
    def log(*args, **kwargs):
        """
        Logging
        :param args:
        :param kwargs:
        :return:
        """
        print(f'{func.__name__} was called; ({args}, {kwargs}). The func returns {func(*args, **kwargs)}')
        return func(*args, **kwargs)

    return log


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


print(func(4, 4, 4))


# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.
def type_check(correct_type):
    def type_checking(func):
        def inner(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                print(f"Wrong Type: {type(arg).__name__}")

        return inner

    return type_checking


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
