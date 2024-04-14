n, m, a = map(int, input().split())
A = [[i for i in input().split()] for _ in range(n)]
if a % 4 == 0:
    for i in A:
        print(' '.join(i))
else:
    for step in range(a % 4):
        A = [[A[-(j + 1)][i] for j in range(len(A))] for i in range(len(A[0]))]
    for i in A:
        print(' '.join(i))
