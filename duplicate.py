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
s=set()
k=0
v="shivaprasad"
for i in range(len(v)):
    if(v[i] in s):
        k+=1
    else:
        s.add(v[i])
print(k)
    
            
            
            
            
