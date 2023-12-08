#!/usr/bin/env python3

""" A function that multiplies a float by the specified multiplier. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns:
    Callable[[float], float]: A function that takes a float
    as input and returns the product.
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
