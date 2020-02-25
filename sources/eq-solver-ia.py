from fractions import Fraction #To implement algorithm without messing floats
from decimal import Decimal
import math
import sys#For CLI input
#Factor finder
def factor(arg1):
   factor = {1}
   divisor = 2
   while divisor <= abs(arg1):
      if arg1%divisor == 0 :
         factor.add(divisor)
      divisor = divisor + 1
   return factor

#Plotter
def plot(x, coefficient_list):
   y = 0
   for j in range(len(coefficient_list)):
      y = coefficient_list[j]*x**(len(coefficient_list) -1 -j) + y
   return y

def plusminus(inputlist):
    outputlist = inputlist + list(map(lambda x: x*(-1), inputlist))
    return outputlist

input_list = list(map(float,input("Values of coefficients: ").split()))#List of coefficients
result = set()
a = input_list[0]
t =-1
if input_list[-1] == 0:
    result.add(0)
while input_list[t] == 0:#Constant or coefficient of smallest term
    t = t-1
c = input_list[t]
while math.ceil(c) != c  or math.ceil(a) != a:
   c =c*10
   a =a*10
   inlist=list(map(lambda num: num*10, inlist))
f_of_a = plusminus(list(factor(a)))
f_of_c = plusminus(list(factor(c)))

for w in range (len(f_of_c)): #Running the algorithm, the algorithm is described in README.md
   for q in range (len(f_of_a)):
       z =  Fraction(f_of_c[w], f_of_a[q])
       if plot(float(z), input_list ) == 0:
         result.add(z)
print(' , '.join(list(map(str,result))))
