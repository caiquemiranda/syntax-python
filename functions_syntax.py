"""
syntax template functions

def function_name(parameters)
    some code

def function_name(parameters, named_defalt_parameter=value):
    some code

"""


def add_two1(a, b):
    c = a + b
    return c


def add_two2(a, b):
    return a + b


print(add_two1(1, 3))
print(add_two2(1, 3))


def shout(exclamation='Hey'):
    print(exclamation)


print(shout())
print(shout('Watch out!'))
