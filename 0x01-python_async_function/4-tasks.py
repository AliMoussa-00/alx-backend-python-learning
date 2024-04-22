#!/usr/bin/env python3
'''Tasks'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Asynchronously spawns 'n' instances of 'task_wait_random' coroutine with the specified 'max_delay',
    gathers their results concurrently, and returns a sorted list of delay values.

    Parameters:
        n (int): The number of times to spawn 'task_wait_random' coroutines.
        max_delay (int): The maximum delay value for each 'task_wait_random' coroutine.

    Returns:
        List[float]: A list of delay values (floats) in ascending order.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(0, n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
