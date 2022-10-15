"""
syntax template functions obj

"""
"""
syntax template functions obj

"""

def say_hello(name):
    return 'Hello ' + name

fow = say_hello('Alice')
print(fow)

fun = say_hello()
print(fun)

bob = fun('Bob')
print(bob)

# 
def say_hello(name, greeter, greeted):
    return "Hello " + greeted + ", I'm " + greeter + "."

print(say_hello('Alice', 'Bob'))

#continue