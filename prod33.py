a=[5,3,20,10,1,4,2]
p = 60  
found = False
unique_triplets = set()

# Iterate through possible values of i, j, k ensuring that each is within bounds
for i in range(len(a)):
    for j in range(i+1):
        for k in range(j+1):
            if i * j * k == p:
                found = True
                # Use a sorted tuple to avoid counting permutations of the same triplet
                triplet = tuple(sorted((i, j, k)))
                unique_triplets.add(triplet)
                print(f'Triplet found: {triplet} - Total unique count so far: {len(unique_triplets)}')

if not found:
    print(-1)
else:
    print(f'Total unique triplets count: {len(unique_triplets)}')
