a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(a)
m = len(a[0])
an = [[0] * n for _ in range(m)]

for row in range(n):
    for col in range(m):
        an[col][row] = a[row][col]

print(an)

