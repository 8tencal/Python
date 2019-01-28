# Function examples in Python
# __author__ = Emmanuel DE LEON
# __license__ =
# __version__ = 0.1


# Simple function call

def my_function(a, b):
        print(a, b)


my_function(1, 2)
my_function(b=2, a=2)

# Optional arguments example (Giving a value on definition turns the argument in optional)


def my_function2(a, b=6, c=5, d=6):
    print(a+b+c+d)


my_function2(8)
my_function2(8, c=6)

# list and dictionary as argument : * and  **
list1 = [1, 2, 3, 4]
dictionary1 = {"a": 5, "b": 7, "c": 8, "d": 9}

my_function2(*list1)
my_function2(**dictionary1)

# Multiple arguments with args and kwargs, unknown size of args as a list, unknown size of kwargs as dictionary


def my_function3(param, *args, **kwargs):
    print("parameter :", param)
    # check args
    if args:
        for val in args:
            print("args : ", val)

    if kwargs:
        for key, val in kwargs.items():
            print("kwargs ", key, val, sep=" : ")


my_function3("param1", "arg1", "arg2", option1="value1", option2="value2")


