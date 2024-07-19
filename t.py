n=["sampath"]
k=1
for i in range(len(n)-1):
    for j in range(i):
        if n[i]==n[j] and k>=1:
            k=k+1
            print('k')
        k=1
        
else:
    print('gg')
print(n.max())
    
            
            
            
            
