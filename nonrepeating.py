a = [1, 1, 2, 2, 3]
r= a[0]

for i in range(1,len(a)):  # Iterate up to the second-to-last element(a[i] ^ a[i+1])
    r=r^a[i]
print(r)
