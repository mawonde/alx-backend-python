#!/usr/bin/env python3

""" A function that  Returns a list of tuples 
where each tuple contains an element from the 
input list and its corresponding length.
    """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns:
    List[Tuple[str, int]]: A list of tuples where
    each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]
