#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    if a_dictionary is None or a_dictionary == {}:
        return None
    lst = sorted(a_dictionary.values())
    score = lst[-1]
    for k in a_dictionary:
        if a_dictionary[k] == score:
            return k
