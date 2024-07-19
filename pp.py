arr=[1,2,1,1,1,1,1,3,4,5]

def find_majority_element(arr):
    # Write your code here.
    umap = {}
    arr=[1,2,1,1,1,1,1,3,4,5]

    for i in range(len(arr)):
        if arr[i] in umap:
            umap[arr[i]] += 1
        else:
            umap[arr[i]] = 1

        if umap[arr[i]] > len(arr) // 2:
            return arr[i]

    return -1
print(find_majority_element(arr))
