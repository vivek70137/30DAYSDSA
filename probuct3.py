a=[1,2,3,4,5,6,7,8]
p=24  
c=0
found=False
s=set()
for i in range(len(a)):
    for j in range(i+1):
        for k in range (j+1):  
           if i*j*k==p:
               found =True
               c+=1
               print(i,j,k,'-',c)
               
if not found:
    print(-1)
