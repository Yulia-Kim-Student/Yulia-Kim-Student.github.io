N, K = map(int, input().split())
marks = input().split()
training_set = [input().split() for i in range(N)]
M = int(input())
test_set = [input().split() for i in range(M)]

marks_for_classes = {i: {} for i in marks}
for example in training_set:
    for i, value in enumerate(example[:-1]):
        mark = marks[i]
        clas = example[-1]
        if value not in marks_for_classes[mark]:
            marks_for_classes[mark][value] = {'0': 0, '1': 0}
        marks_for_classes[mark][value][clas] += 1

mark_rules = {}
for mark, values in marks_for_classes.items():
    mark_rules[mark] = {}
    for value, counts in values.items():
        if counts['0'] == counts['1']:
            predicted_class = '1'
        else:
            predicted_class = max(counts, key=counts.get)
        mark_rules[mark][value] = predicted_class

mark_error = {mark: 0 for mark in marks}
for example in training_set:
    for i, value in enumerate(example[:-1]):
        mark = marks[i]
        if mark_rules[mark][value] != example[-1]:
            mark_error[mark] += 1

one_rule = min(mark_error, key=mark_error.get)

for example in test_set:
    value = example[marks.index(one_rule)]
    predicted_class = mark_rules[one_rule].get(value, '1')
    print(predicted_class)