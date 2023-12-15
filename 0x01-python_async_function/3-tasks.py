#!/usr/bin/python3
"""asynchronous coroutine that takes
in an integer argument"""
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Creates an asyncio Task for the wait_random coroutine.

    Parameters:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        asyncio.Task: The asyncio Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
