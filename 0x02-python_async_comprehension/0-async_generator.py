#!/usr/bin/env python3

"""
This module defines an asynchronous
generator coroutine that yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loops 10 times,
    asynchronously waits for 1 second,
    then yields a random number between 0 and 10.

    :return: None
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
