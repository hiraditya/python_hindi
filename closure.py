# How to define and use a closure

def gen_multiplier():
    x = 10 # non-local variable
    def multiplier(y): # stores the reference to non-local variables
        return x*y #x is non local to multiplier

    return multiplier

# call the function
m = gen_multiplier()

del gen_multiplier

k = gen_multiplier()

# call the returned function
print(m(5))

# nested-function
# nested function should access non-local variable
# it should return the en-closed function