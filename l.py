
n=int(input("enter"))
arr=list(map(int,input().strip().split()))

for i in range(len(arr)-1):#use -1 when we are using like[i+1]
    if(arr[i]<arr[i+1]):
        arr[i]=arr[i+1]
print(arr[i])        

