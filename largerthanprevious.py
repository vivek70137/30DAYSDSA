a=[7,4,8,2,9]
s=a[0]
c=1
ma=s
for i in range(len(a)):
    if a[i]>s:
        s=a[i]
        c+=1
print(c)        
        
