a=[1,2,5,2,1]
r=sum(a)
l=0
for i,n in enumerate(a):
    r-=n
    if l==r:
      print(i)
      break
    l+=n    
    
else:
    print(-1)
