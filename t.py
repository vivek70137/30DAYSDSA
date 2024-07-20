n = ["sampaaath", "sampaaath", "another", "another", "another"]
k = 0

# Use a set to keep track of seen elements
seen = set()

for i in range(len(n)):
    if n[i] in seen:
        k += 1
    else:
        seen.add(n[i])

print(k)
    
            
            
            
            
