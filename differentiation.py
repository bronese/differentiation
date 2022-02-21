import math
def differentiation(a,n):
   if n==1:
      return a
   elif n==0 or a==0:
      return 0
   else:
      an1=a*n
      an1=str(an1)
      b=n-1
      b=str(b)
      return an1+"x^"+b
   
def error_code (a,n):
   if not(str.isnumeric(a)): 
      print(a+" is not a float")
         a=input("input 'a' value")
   elif not(str.isnumeric(n)):
      print (n+" is not a float")
   elif not(str.isnumeric(a)) and not(str.isnumeric(n)):
      print (a+" and "+n+" is not a float")

a=input("input 'a' value")
while not(str.isnumeric(a)):
   print (error_code(a))
n=input("input 'n' value")
if not(str.isnumeric(n)):
   print (error_code(a,n))


a=float(a)
n=float(n)
print(differentiation(a,n))

