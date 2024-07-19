def m(n):
    maxsub=n[0]
    curr=0
    for i in (n):
        if curr<0:
            curr=0
        curr+=i
        maxsub=max(maxsub,curr)
    return maxsub    
n=[-2,1,-3,4,-1,2,1,-5,4]
v=m(n)
print(v)
        
