#!/usr/bin/env python3
'''Let's execute multiple coroutines at the same time with async'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Asynchronously spawns 'n' instances of 'wait_random' coroutine with
    the specified 'max_delay', gathers their results concurrently,
    and returns a sorted list of delay values.

    Parameters:
        n (int): The number of times to spawn 'wait_random' coroutines.
        max_delay (int): The maximum delay value for each 'wait_random'.

    Returns:
        List[float]: A list of delay values (floats) in ascending order.

    '''
    tasks = [wait_random(max_delay) for _ in range(0, n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
