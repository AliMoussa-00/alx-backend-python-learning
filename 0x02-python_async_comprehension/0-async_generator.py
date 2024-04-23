#!/usr/bin/env python3
'''Async Generator'''


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Asynchronously generates random floating-point numbers between 0 and 10.

    This async generator yields random floating-point numbers between 0 and 10
    at one-second intervals asynchronously using asyncio.sleep.

    Yields:
        float: A random floating-point number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
