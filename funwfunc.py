# Odd Even

def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number."
        else:
            print "Number is " + str(i) + ". This is an odd number."

odd_even()

# Multiply
def multiply(b, a):
    newlist = []
    for i in b:
        newlist.append(i*a)
    return newlist

# hacker
def layered_mult(arr):
    newarr = []
    for row in arr:
        newarr.append([row/row]*row)
    print newarr

layered_mult(multiply([2,4,5],3))