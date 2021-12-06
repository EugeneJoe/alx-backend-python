#!/usr/bin/env python3
"""
Contains a coroutine that takes in an integer argument and waits
for a random delay between 0 and that integer arguments seconds
and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine that takes in an integer and waits for a random delay between 0
    and that integer argument seconds and returns it
    """
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
