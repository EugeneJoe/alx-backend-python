#!/usr/bin/python3
"""
Chaining multiple coroutines
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """chain multiple coroutines"""
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return res
