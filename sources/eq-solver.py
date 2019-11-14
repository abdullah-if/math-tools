from fractions import Fraction
from decimal import Decimal
import sys
def factor(arg1):
   l = [1]
   a = 2
   while a <= (abs(arg1))**.5:
      if arg1%a == 0 :
         l.append(a)
      a = a + 1
   return l
def plot (o, d, t, dlist):
   y = 0
   xlist=[]
   fxlist=[]
   r = o
   while o<= r and r<= d: #Putting all the values in function of x
      for j in range(len(dlist)):#"Defining" the function of x in r
         y = dlist[j]*r**(len(dlist) -1 -j) + y
         xlist.append(r)
         fxlist.append(y)
         y = 0 #This stops the previous value of f(x) to be added in sub>
         r = float(Decimal(r) + Decimal(t)) #Decimal function is used to>
   return xlist, fxlist
def mark(lm, qlist):
   kj = 0
   for re in range(len(qlist)):
      kj = qlist[re]*lm**(len(qlist) -1 -re) + kj
   return kj
inlist = list(map(float, input("Values of coefficient").split()))
zlist =[]
a = inlist[0]
t =-1
while inlist[t] == 0:
    t = t-1
    zlist.append(0)
c = inlist[t]  
n = 2
alist =[*factor(a), *list(map(lambda x: x*(-1), (factor(a))))]
clist =[*factor(c), *list(map(lambda x: x*(-1), (factor(c))))]
for w in range (len(clist)):
   for q in range (len(alist)):
       z =  Fraction(clist[w], alist[q])
       if mark(float(z), inlist ) ==0:
         zlist.append(z)
         
print(list(set(map(float,(zlist)))))
