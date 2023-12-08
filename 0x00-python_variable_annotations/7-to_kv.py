#!/usr/bin/env python3

""" Creates a tuple with the string k and the square of the int/float v. """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns:
    Tuple[str, float]: A tuple with the string k and the square of v as a float.
    """
    return k, float(v**2)
