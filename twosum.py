def twoSum(arr, n, target):
    ind = {}
    
    for i in range(n):
        comp = target - arr[i]
        if comp in ind:
            return [ind[comp], i]
        ind[arr[i]] = i
    
    return [-1, -1]

result = twoSum([2, 7, 11, 15], 4, 17)
print(result)  
