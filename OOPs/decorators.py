# Decorators in Python
# Takes a function as argument and returns an enhanced version of it.

"""
def decFun(f):
    def innerFun():
        print("Welcome")
        f()
    return innerFun

def fun():
    print("User")

fun = decFun(fun)
fun()
"""

#######################################################################

# Short Syntax (@)

def decFun(f):
    def innerFun():
        print("Welcome")
        f()
    return innerFun

@decFun
def fun():
    print("User")
fun()

