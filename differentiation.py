import math
def differentiation(A,N):
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
   
def error_code (x,y):
   if not(str.isnumeric(x)): 
      print(x+" is not a float")
   elif not(str.isnumeric(y)):
      print (y+" is not a float")

a=input("input 'a' value")
n=input("input 'n' value")
while not(str.isnumeric(a)) or not(str.isnumeric(n)):
   print(error_code(a,n))
if (str.isnumeric(a)) and (str.isnumeric(n)):
   a=float(a)
   n=float(n)
   print(differentiation(a,n))