from fractions import Fraction #To implement algorithm without messing floats
from decimal import Decimal
from math import ceil
import sys#For CLI input

def factor(arg1):#Factor finder
   factor = {1}
   divisor = 2
   while divisor <= abs(arg1):
      if arg1%divisor == 0 :
         factor.add(divisor)
      divisor = divisor + 1
   return factor

def plot(x, coefficient_list): #Plotter
   y = 0
   for j in range(len(coefficient_list)):
      y = coefficient_list[j]*x**(len(coefficient_list) -1 -j) + y
   return y

def plusminus(inputlist): #Plusminus
    outputlist = inputlist + list(map(lambda x: x*(-1), inputlist))
    return outputlist

input_list = list(map(float,sys.argv[1:]))
result = set()
a = input_list[0]
t =-1
if input_list[-1] == 0:
    result.add(0)
while input_list[t] == 0:#Constant or coefficient of smallest term
    t = t-1
c = input_list[t]
while ceil(c) != c  or ceil(a) != a:
   c =c*10
   a =a*10
   inlist=list(map(lambda num: num*10, inlist))
f_of_a = plusminus(list(factor(a)))
f_of_c = plusminus(list(factor(c)))

for div_coff in range (len(f_of_c)): #Running the algorithm, the algorithm is described in README.md
   for div_lead in range (len(f_of_a)):
       sol =  Fraction(f_of_c[div_coff], f_of_a[div_lead])
       if plot(float(sol), input_list ) == 0:
         result.add(sol)
print(' , '.join(list(map(str,result))))
