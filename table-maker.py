import sys
from decimal import Decimal, getcontext
getcontext().prec= 3
inlist = list(map(float,sys.argv[1:]))
u = inlist.pop(-3)
v = inlist.pop(-2)
s = inlist.pop(-1)
x = u
y=0
xlist=[]
fxlist=[]
while u<= x and x<= v:
        for j in range(len(inlist)):
            y = inlist[j]*x**(len(inlist) -1 -j) + y
        xlist.append(x)
        fxlist.append(y)
        y = 0
        x = float(Decimal(x) + Decimal(s))
print ("x\tf(x)")
for i in range(len(xlist)):
    print ( "%.3f\t%.3f" %(xlist[i], fxlist[i]))
