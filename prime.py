c=0
n=4
t=0
def f(n):
  for i in range(2,n):
    if n%i==0:
       return False
    return True
  
    
    
def v(n):
   for i in range(2,n+1):
    if f(n):
        t+=n
        return t
print (v(n))
