#!/usr/bin/env python3
'''Measure the runtime'''

import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the average execution time per coroutine for the wait_n function.

    Parameters:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay value for each coroutine.

    Returns:
        float: The average execution time per coroutine, in seconds.

    '''
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()

    return (end_time - start_time) / n
