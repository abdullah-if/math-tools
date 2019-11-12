import cmath #In case of complex solution, for avoiding +j part use math in all instances
import sys #For getting input from CLI
def qud(arg1, arg2, arg3): #Defining the function
    x1 = (-arg2 + cmath.sqrt(arg2**2 - 4*arg1*arg3))/(2*arg1) 
    x2 = (-arg2 - cmath.sqrt(arg2**2 - 4*arg1*arg3))/(2*arg1)
    return x1, x2 g
print(qud(*map(float, sys.argv[1:])))
""" All in one line, first transforming all argument vectors in float, passing them through 
the defined function and printing the outputs. I'm a bit lazy. :) """
