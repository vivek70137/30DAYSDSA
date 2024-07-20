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
    
a=[1,2,3,2,1]#or
r=sum(a)
l=0
for i in range(len(a)):
    r-=a[i]
    if l==r:
        print(i)
        break
    l+=a[i]
else:
    print(-1)
