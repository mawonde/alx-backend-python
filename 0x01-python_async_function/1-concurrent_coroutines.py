#!/usr/bin/python3

""" Asynchronous routine that spawns wait_random
n times with the specified max_delay."""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """

    Parameters:
        n (int):  Default is 10.

    Returns:
        list[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
