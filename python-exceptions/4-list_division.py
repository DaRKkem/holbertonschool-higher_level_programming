#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element two lists safely and return a new list."""
    result = []
    for i in range(list_length):
        res = 0
        try:
            try:
                res = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(res)
    return result
