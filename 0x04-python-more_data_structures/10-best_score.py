#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    for i in a_dictionary.items():
        if i > max:
            max = i
    return max

    
