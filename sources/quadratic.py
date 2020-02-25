from cmath import sqrt#In case of complex solution
import sys #For getting input from CLI
def qudratic(a, b, c): #Defining the function
    d = b**2 - 4*a*c
    if d >=0:
        x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    else :
        x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2
print(qudratic(*map(float, sys.argv[1:])))
""" All in one line, first transforming all argument vectors in float, passing them through
the defined function and printing the outputs. I'm a bit lazy. :) """
