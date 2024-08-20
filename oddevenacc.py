a=[1,2,3,4,5,6]
v=''
if len(a)<0:
    print(-1)
for i in range(len(a)):
    if a[i]%2==0:
        v+='even'
    elif a[i]%2!=0:
        v+='odd'
print(v)
