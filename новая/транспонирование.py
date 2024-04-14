# a = int(input())
# A = [[i for i in map(int, input().split())] for _ in range(a)]
a = 3
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
C = [[A[j][i] for j in range(a)] for i in range(a)]
for i in range(a):
    print(' '.join(map(str, (C[i]))))


