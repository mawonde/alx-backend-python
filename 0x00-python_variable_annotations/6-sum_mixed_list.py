#!/usr/bin/env python3

""" Calculates the sum of a list of integers and floats. """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
     Returns:
    float: The sum of the input list of integers and floats.
    """
    return sum(mxd_lst)
