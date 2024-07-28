def nn(n):
    a=int(n[0])
    i=1
    while i<len(n):
        if n[i]=='A':
            a&=int(n[i+1])
        elif n[i]=='B':
            a|=int(n[i+1])
        elif n[i]=='c':
            a^=int(n[i+1])
        i+=2
    return a
print(nn("1A1"))    


