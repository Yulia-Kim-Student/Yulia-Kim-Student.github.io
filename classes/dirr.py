a = eval(input())
public = [i for i in dir(a) if i[0] != '_']
private = [i for i in dir(a) if i[0] == '_']
for i in sorted(public):
    print(i)
for i in sorted(private):
    print(i)
