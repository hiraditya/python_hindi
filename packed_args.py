# How to pass packed arguments to a function

def amt(p, r, t):
    return p + p*r*t/100

#     r,    p, t
d = [10, 1000, 2]

def amt_adaptor(r, p, t):
    return amt(p, r, t)

print(amt_adaptor(*d))