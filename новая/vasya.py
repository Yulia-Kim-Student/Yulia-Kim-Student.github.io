file = open('../np/input.txt')
D, T = map(float, file.readline().split())
v_l = list(map(float, file.readline().split()))
w_l = list(map(float, file.readline().split()))
list = []
for w in w_l:
    for v in v_l:
        if v != w:
            t1 = (D - T * w) / (v - w)
            if t1 > 0 and t1 * v < D:
                list.append(t1 * v)
        else:
            if v * T == D:
                list.append(D)
if list == []:
    print(0, file=open('output.txt', 'w'))
else:
    print(round(max(list), 4), file=open('output.txt', 'w'))

