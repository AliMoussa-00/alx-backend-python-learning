#!/usr/bin/env python3
'''Async Comprehensions'''

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Asynchronously generates a list of random floating-point numbers.

    This function asynchronously generates a list of random floating-point
    numbers by iterating over the async generator returned by async_generator()

    Returns:
        List[float]: A list of random floating-point numbers.
    '''
    return [rand async for rand in async_generator()]
