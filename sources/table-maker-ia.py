from decimal import Decimal, getcontext
"""I wanted to avoid importing this module but, the floats were messing up like
>>> 1-0.8
0.19999999999999996
So, I used it. Round function could helped. But using that produce  -0.000, which seemed unaesthetic to me."""
getcontext().prec= 3 #Useless, since used %.3f at end.
def table (start, end, step, coefficient_list):
   y = 0
   xlist=[]
   fxlist=[]
   x = start
   while start<= x and x<= end:
      for j in range(len(coefficient_list)):
         y = coefficient_list[j]*x**(len(coefficient_list) -1 -j) + y
      xlist.append(x)
      fxlist.append(y)
      y = 0
      x = float(Decimal(x) + Decimal(step))
   print ("x\tf(x)")
   for i in range(len(xlist)): #Printing in two columns, each column is 1 tab appart. (As long as the value of x lesser than 7 character.
       print ( "%.3f\t%.3f" %(xlist[i], fxlist[i]))

table(float(input("Starting point :")),float(input("End point :")),float(input("Step :")),list(map(float, input("Coefficients :").split())))
