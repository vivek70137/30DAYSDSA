def matrix_sum(N, M, Grid):
    total_sum = 0
    for i in range(N):
        for j in range(M):
            total_sum += Grid[i][j]
    return total_sum

# Example usage:
N = 1
M = 2
Grid = [
    [1, 0, 1],
    [-8, 9, -2]
]

print(matrix_sum(N, M, Grid))  # Output: 1
