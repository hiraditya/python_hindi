# How to write a decorator ( a wrapper around another function )

def add_num_decorate(f):
    def wrap_add_num(i, j):
        print("<p>")
        print("Sum=", f(i, j))
        print("</p>")
    return wrap_add_num

# Functions in python are first class citizens
# <p> </p>

@add_num_decorate
def add_num(i, j): # add two numbers
    return i+j


add_num(10, 25)