def s(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f   
a='aeiouAEIOU'
c=0
arr='abbh'
for i in range(len(arr)):
    if arr[i] not in a:
        c+=1
d=s(c)
print(d)
