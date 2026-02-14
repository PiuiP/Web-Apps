n = int(input())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

C = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))

for row in C:
    print(' '.join(map(str, row)))