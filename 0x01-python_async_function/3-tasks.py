#!/usr/bin/python3
"""
Create an async task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Returns an asyncio.Task object"""
    return asyncio.create_task(wait_random(max_delay))
