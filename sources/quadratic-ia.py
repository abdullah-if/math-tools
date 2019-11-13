import cmath #In case of complex solution, for avoiding +j part use math in all instances
def qud(arg1, arg2, arg3): #Defining the function
    x1 = (-arg2 + cmath.sqrt(arg2**2 - 4*arg1*arg3))/(2*arg1) 
    x2 = (-arg2 - cmath.sqrt(arg2**2 - 4*arg1*arg3))/(2*arg1)
    return x1, x2 
print(qud(*map(float, input( "Values of coeffecients: \n").split())))
""" All in one line, first taking input, splitting the string, turning inputs
 in float, passing them through the defined function and printing the outputs.
 I'm a bit lazy. :) """
