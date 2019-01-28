# Condition examples in Python
# __author__ = Emmanuel DE LEON
# __license__ =
# __version__ = 0.1

a = True

if a is True:
    print("true")
else:
    print("false")

# Test with different operators
b = 5
c = 6

if b is not 6:
    print("b is not 6")

# test with else if

if b != 5:
    print("b is different from 5")
elif b <= 5: # =>
    print("b is lower or equal to 5")
else:
    print("final else body")

if c == 6:
    print("equal values")



