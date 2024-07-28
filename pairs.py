arr=[1,2,4,8,6]
t=2
c=0
for i in range(len(arr)):
   if arr[i]-t in arr:
      c+=1
print(c) 
