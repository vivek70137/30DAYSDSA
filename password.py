def nu(n):
    c=0
    f=0
    d=0
    if len(n)<4:
        return 0
    if n[0].isdigit():
        return 0
    for i in range(len(n)):
        if n[i]>='A' and n[i]<='Z':
            c+=1
        elif n[i].isdigit():
            f+=1
        elif n[i]!=" "and n[i]!='/' :
            d+=1
             
    return 1 if c>0 and d>0 and f>0 else 0
n='Bb1gj'
print(nu(n))