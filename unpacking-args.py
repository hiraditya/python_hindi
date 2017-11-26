# Unpacking arguments of functions
def si(p, r, t):
    return p*r*t/100

def amt(r, t, p):
    return p+p*r*t/100

# Forwarding function, adaptor
def amt1(p, r, t):
    return amt(r, t, p)

d1 = [1000, 10, 2]

#s1 = si(*d1)
#print(s1)

print(amt1(*d1))
