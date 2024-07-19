arr = [1,2,3,-2,-4,-2,4]
llist = set()
for i in range(len(arr)):
    for j in range(i+1,len(arr)-1):
        for k in range(j+1,len(arr)-1):
            for l in range(k+1,len(arr)-1):
               if (arr[i]+arr[j]+arr[k]+arr[l] == 0):
                 llist.add((arr[i],arr[j],arr[k],arr[l]))
print(llist)
