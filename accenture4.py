n=int(input())
m=int(input())
s=0
v=0
for i in range(1,m+1):
    if i%n==0:
        s+=i
    else:
        v+=i
f=v-s
print(f)
