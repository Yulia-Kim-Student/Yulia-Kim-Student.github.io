# import numpy as np
# # random_list = [[random.uniform(0.0, 10.0), random.uniform(0.0, 10.0)] for _ in range(5)]
# # print(random_list)
# a = 1.12425
# r_distance = np.round(a, 4)
# # print(np.remainder(r_distance, 1))
# print(r_distance)
# # if np.floor(r_distance) % 2 == 1 and np.remainder(r_distance, 1) == 0.5:
# #     r_distance = np.round(a - 0.5 * 10 ** (-4), 4)
# # print(r_distance)
a = input()
public = [i for i in dir(a) if i[0] != '_']
private = [i for i in dir(a) if i[0] == '_']
for i in sorted(public):
    print(i)
for i in sorted(private):
    print(i)