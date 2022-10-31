def test(text):
    l = []
    l.append(text)
    return l

def test1(test):
    return test

def dec(func):
    txt = func("hello")
    print(txt)
#driver code.
dec(test)

# What mean by decorators

# a decorator can change the behaviour of an object
#  Decorators allow us to wrap another function in order 
# to extend the behaviour of the wrapped function, without permanently modifying it.



