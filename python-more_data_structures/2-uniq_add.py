#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    copy = []
    for element in my_list:
        copy.append(element)
        result += element
        print(result)
    return result
