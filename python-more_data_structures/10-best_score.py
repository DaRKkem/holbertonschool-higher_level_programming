#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = next(iter(a_dictionary))
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[best]:
            best = key
    return best
