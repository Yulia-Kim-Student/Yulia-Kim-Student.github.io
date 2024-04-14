import sys
import pprint
file = open('input.txt')
N, M, K = map(int, file.readline().split())
tu_machine = {}
for p in range(N):
    tu_machine[p] = file.readline().split()
for i in tu_machine.keys():
    tu_machine[i] = {c: tu_machine[i][c*3:c*3+3] for c in range(0, M)}

k = [int(i) for i in file.readline().split()]
status = 0
index = 0

while status != M:
    a = tu_machine[k[index]][status]
    k[index], status = int(a[0]), int(a[2])
    if a[1] == 'N':
        index = index
    elif a[1] == 'R':
        index += 1
    else:
        index += -1
    if index < 0:
        index = 0
        k.insert(0, 0)
    if index > len(k) - 1:
        k.append(0)
print(*k[index::], file=open('output.txt', 'w'))
