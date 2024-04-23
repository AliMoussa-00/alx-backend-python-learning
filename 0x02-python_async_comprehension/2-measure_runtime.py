#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the total runtime of executing async comprehensions multiple times

    This function measures the total runtime of executing 'async_comprehension'
    function asynchronously multiple times using asyncio.gather().

    Returns:
        float: The total runtime in seconds.

    '''
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    return (time.time() - start_time)
