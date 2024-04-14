with open('../np/input.txt', 'r') as name:
    variable = name.read()
words = []
word = ""
if variable[0].isupper():
    for a in variable:
        if a.isupper() and word:
            words.append(word.lower())
            word = a
        else:
            word = word + a
    words.append(word.lower())
    print('_'.join(words), file=open('../np/output.txt', 'w'))
else:
    for a in variable:
        if a == '_' and word:
            words.append(word[0].upper() + word[1:])
            word = ''
        else:
            word = word + a
    words.append(word[0].upper() + word[1:])
    print(''.join(words), file=open('../np/output.txt', 'w'))

