#!/usr/bin/env python3

"""
This module defines an asynchronous
generator coroutine and a coroutine that collects
10 random numbers using async comprehension.
"""


from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using
    async comprehension over async_generator.

    :return: List of 10 random numbers
    :rtype: List[int]
    """
    # Using async comprehension to collect 10 random numbers
    nums = [num async for num in async_generator()]

    return nums
