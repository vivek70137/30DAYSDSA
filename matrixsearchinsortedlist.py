a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t=4
l=0

row=len(a)
col=len(a[0])
h=row*col-1
while (l<=h):
    m=(l+h)//2
    midval=a[m//col][m%col]
    if midval==t:
        print("true",t)
        break
    elif midval < t:
        l=m+1
    else:
        h=m-1
else:
    print('false')
    
