#!/usr/bin/python3
for i in range(0, 9): # 9 et pas 10 car 90 ou + jamais atteint (89 max, où i = 8)
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
