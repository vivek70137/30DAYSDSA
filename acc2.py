n=int(input("enter"))
m=list(map(int,input().rstrip().split()))
maxu=0
for i in range(1,len(m)):
    if m[i]<m[i+1]:
        m[i+1]=maxu
print(maxu)        
    
