from fractions import Fraction #To implement algorithm without messing floats
from decimal import Decimaal
def factor(arg1):#Factor finding function
   l = [1]
   a = 2
   while a <= (abs(arg1))**.5:
      if arg1%a == 0 :
         l.append(a)
      a = a + 1
   return l
def plot (o, d, t, dlist):#Table maker function, for comments goto table-maker.py
   y = 0
   xlist=[]
   fxlist=[]
   r = o
   while o<= r and r<= d: 
      for j in range(len(dlist)):
         y = dlist[j]*r**(len(dlist) -1 -j) + y
         xlist.append(r)
         fxlist.append(y)
         y = 0 
         r = float(Decimal(r) + Decimal(t))
   return xlist, fxlist
def mark(lm, qlist):#Table maker function modified for finding point
   kj = 0
   for re in range(len(qlist)):
      kj = qlist[re]*lm**(len(qlist) -1 -re) + kj
   return kj
inlist = list(map(float,input("Values of coefficients: ").split())#List of coefficients 
zlist =[]
a = inlist[0]#Leading coefficient 
t =-1
while inlist[t] == 0:#Constant or coefficient of smallest term
    t = t-1
    zlist.append(0)
c = inlist[t]  
n = 2
alist =[*factor(a), *list(map(lambda x: x*(-1), (factor(a))))]#Factors of leading coefficient 
clist =[*factor(c), *list(map(lambda x: x*(-1), (factor(c))))]#Factors of constant or smallest coefficient 
for w in range (len(clist)): #Running the algorithm, the algorithm is described in README.md
   for q in range (len(alist)):
       z =  Fraction(clist[w], alist[q])
       if mark(float(z), inlist ) ==0:
         zlist.append(z)
         
print(list(set(map(float,(zlist)))))#Getting the result as set, each domain once.
