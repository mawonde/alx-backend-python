#!/usr/bin/python3
"""Asynchronous routine that spawns wait_random
n times with the specified max_delay."""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random
    n times with the specified max_delay.


    Returns:
        list[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)
    return sorted([task.result() for task in tasks])
