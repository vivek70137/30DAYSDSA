a='10110111'
b=0
ans=''
for i in range(len(a)):
    if a[i]=='1':
        b+=1
    else:
        if b>0:
            ans+=chr(64+b)
            b=0
if(b>0):
    ans+=chr(64+b)
print(ans)    
