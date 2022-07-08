#!/usr/bin/python3
"""Module to find the max integer in a a_list
"""


def max_integer(a_list=[]):
    """Function to find and return the max integer in a a_list of integers
        If the a_list is empty, the function returns None
    """
    if len(a_list) == 0:
        return None
    result = a_list[0]
    i = 1
    while i < len(a_list):
        if a_list[i] > result:
            result = a_list[i]
        i += 1
    return result
