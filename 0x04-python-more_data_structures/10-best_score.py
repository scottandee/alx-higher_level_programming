#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    values = a_dictionary.values()
    maxim = max(values)
    for i in  a_dictionary.items():
        if i[1] == maxim:
            return i[0] 
