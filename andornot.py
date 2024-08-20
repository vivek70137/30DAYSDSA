str='1C01A1C0'
a=int(str[0])
i=1
for i in range (len(str)):
        if str[i]=='A':
            a =a & int(str[i+1])
        elif str[i]=='B':
            a |=int(str[i+1])
        elif str[i] == 'C':
            a ^=int(str[i+1])
        i+=2
print(a)
##str = '1C01A1C0'
##a = int(str[0])
##i = 1
##
##while i < len(str):
##    if str[i] == 'A':
##        a &= int(str[i+1])
##    elif str[i] == 'B':
##        a |= int(str[i+1])
##    elif str[i] == 'C':
##        a ^= int(str[i+1])
##    i += 2
##
##print(a)
