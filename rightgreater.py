a=[5,7,1,7,6,0]
n=len(a)
ans=[-1]*n
s=[]
v=0
s.append(a[-1])
a[-1]=-1
for i in range(n-2,-1,-1):
    v=a[i]
    while s and s[-1] <=v:
        s.pop()
    if s:
        ans[i]=s[-1]
    else:
        ans[i]= -1
    s.append(v)
print(ans)


a = [5, 6, 1, 7, 6, 0]
n = len(a)
result = [-1] * n  # Default to -1
stack = []

# Traverse from right to left
for i in range(n - 1, -1, -1):
    # Remove all elements smaller than or equal to current
    while stack and stack[-1] <= a[i]:
        stack.pop()
    
    # If stack is not empty, the top is the next greater element
    if stack:
        result[i] = stack[-1]
    
    # Push current element onto stack
    stack.append(a[i])

print(result)
