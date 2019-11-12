import cmath
import sys
def qud(arg1, arg2, arg3):
    x1 = (-arg2 + cmath.sqrt(arg2**2 - 4*arg1*arg3))/(2*arg1)
    x2 = (-arg2 - cmath.sqrt(arg2**2 - 4*arg1*arg3))/(2*arg1)
    return x1, x2
print(qud(*map(float, sys.argv[1:])))
