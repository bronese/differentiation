import math
def differentiation(A,N):
   if N==1:
      return A
   elif n==0 or a==0:
      return 0
   else:
      an1=A*N
      an1=str(an1)
      b=N-1
      b=str(b)
      return an1+"x^"+b
   
def error_code(a,n): 
   if not(str.isnumeric(a)):
      print(f"{a} is not a numerical response")
   if not(str.isnumeric(n)):
      print(f"{n} is not a numerical response")

# input chunk
a=input("input 'a' value") 
while not(str.isnumeric(a)):
   print(error_code(a))
   if (str.isnumeric(a)):
      break
n=input("input 'n' value")
while not(str.isnumeric(n)):
   print(error_code(n))
   if (str.isnumeric(n)):
      break

if (str.isnumeric(a)) and (str.isnumeric(n)):
   a=float(a)
   n=float(n)
   print(differentiation(a,n))