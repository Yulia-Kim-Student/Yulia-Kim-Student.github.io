# import sys
# field = sys.stdin
def shars(matrix, x, y):
     b = [[matrix[i][j] for i in [x - 1, x, x - len(matrix) + 1]] for j in [y - 1, y, y - len(matrix[0]) + 1]]
     t = 0
     for i in b:
          t += i.count('#')
     return  t
field = open('../np/input.txt')
a = [[i for i in line.strip()] for line in field.readlines()]
b = [['.' for i in a[0]] for _ in a]
for i in range(len(a)):
     for j in range(len(a[0])):
          if (a[i][j] == '.' and (shars(a, i, j) == 3)) or (a[i][j] == "#" and (shars(a, i, j) in [3, 4])):
               b[i][j] = '#'
          else:
               b[i][j] = '.'

for i in b:
     print(''.join(i))
