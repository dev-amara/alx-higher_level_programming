#!/usr/bin/python3
"""
    module for a MyList class that inherits frm list
"""


class MyList(list):
    """
        class that inherits frm list
    """
    def print_sorted(self):
        print(sorted(self))
