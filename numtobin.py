a=10
an=''
if a==0:
    print('0')
if a==1:
    print('1')
while(a>0):
        if (a&1):
            an+='1'
        else:
            an+='0'
        a=a>>1    
print(an)            
            
