#!/usr/bin/env python3
"""
Asynchronous routine that spawns wait_random
n times with the specified max_delay.
"""


import time
from wait_n import wait_n

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Returns:
        float: Average execution time per iteration.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
