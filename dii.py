def dup(arr): 
    v= set()
    li =[]
    for num in arr:
        if num in v:
            li+=[num]
        else:
             v.add(num)
    return li
t=int(input())
for i in range(t):
     N = int(input())
     arr = list(map(int, input().split()))
     li=(dup(arr))
     for i in li:
         print(i,end=" ")
     print()
