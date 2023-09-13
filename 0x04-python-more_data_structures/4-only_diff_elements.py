#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    same = set_1.intersection(set_2)
    new_set = set_1 | set_2
    new_set.difference_update(same)
    return new_set
