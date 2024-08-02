a=[7,1,2,4,50,6,1]
b=a[0]
v=0
s=0
for i in range(1,len(a)):
    if a[i]<b:
        b=a[i]
    v=a[i]-b
    s=max(v,s)
print(s)
