import string
task = open('file').readline()
alphabet = set(string.ascii_letters)
previous = False
words = 0
for i in task:
    if i in alphabet and not previous:
        words += 1
        previous = True
    elif previous:
        previous = (i in alphabet or i == '-')
    else:
        previous = False

print(words, file=open('file', 'w'))
