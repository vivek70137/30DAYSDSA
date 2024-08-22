m=0
c=0
a=[1,1,0,1,1,1,0,1]
for i in range(len(a)):
    if a[i]==1:
        c+=1
        m=max(m,c)
    else:
        c=0
print(m)        
    
