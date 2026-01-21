#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    copy = []
    for element in my_list:
        copy.append(element)
        result += element
        print(result)
    return result

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
