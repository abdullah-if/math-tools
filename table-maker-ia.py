from decimal import Decimal, getcontext
"""I wanted to avoid importing this module but, the floats were messing up like
>>> 1-0.8
0.19999999999999996
So, I used it. Round function could helped. But using that produce  -0.000, which seemed unaesthetic to me."""
getcontext().prec= 3 #Useless, since used %.3f at end.
inlist = list(map(float, input("Coefficients :").split()))#Putting all input in a list, after turning into float
u = float(input("Starting point :"))#Lower limit and starting point
v = float(input("End point :")) #Upper limit
s = float(input("Step :"))#Step deviation 
x = u #First value of x
y=0
xlist=[]
fxlist=[]
while u<= x and x<= v: #Putting all the values in function of x
        for j in range(len(inlist)):#"Defining" the function of x in runtime
            y = inlist[j]*x**(len(inlist) -1 -j) + y
        xlist.append(x)
        fxlist.append(y)
        y = 0 #This stops the previous value of f(x) to be added in subsequent f(x)
        x = float(Decimal(x) + Decimal(s)) #Decimal function is used to avoid floating point mishap
print ("x\tf(x)")
for i in range(len(xlist)): #Printing in two columns, each column is 1 tab appart. (As long as the value of x lesser than 7 character.
    print ( "%.3f\t%.3f" %(xlist[i], fxlist[i]))
