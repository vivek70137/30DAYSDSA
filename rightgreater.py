a=[5,7,1,7,6,0]
n=len(a)
ans=[-1]*n
s=[]
v=0
s.append(a[-1])
a[-1]=-1
for i in range(n-2,-1,-1):
    v=a[i]
    while s and s[-1] <=v:
        s.pop()
    if s:
        ans[i]=s[-1]
    else:
        ans[i]= -1
    s.append(v)
print(ans)
