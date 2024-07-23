str='shiva'
n=2
while(n>0):
    print(str[-n],end='')
n= int(input())
for _ in range(n):
        
        nc=int(input())
        c=0
        coins=list(map(int,input().strip().split()))
        freq=list(map(int,input().strip().split()))
        v=int(input())
        for i in range(nc):
            s=0
            s+=coins[i]
            for j in range(freq[i-1]):
                s+=coins[i]
                if s==v:
                    c+=1
print(c)            
print(s) 
         
