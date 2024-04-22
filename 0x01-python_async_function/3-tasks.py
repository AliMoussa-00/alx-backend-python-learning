#!/usr/bin/env python3
'''Tasks'''

import asyncio
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    '''
    Creates and returns a task that asynchronously executes
    the wait_random coroutine.

    Parameters:
        max_delay (int): The maximum delay value for the 'wait_random'.

    Returns:
        Task: A task that represents the asynchronous execution
        of the wait_random coroutine.

    '''
    return asyncio.create_task(wait_random(max_delay))
