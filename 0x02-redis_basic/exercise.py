#!/usr/bin/env python3
"""python module to interact with redis server"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


class Cache:
    """class to store Redis client information"""

    def __init__(self):
        """ iniitalize Redis DB """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ create a random key & stores it with data """
        key: uuid.UUID = uuid.uuid1()
        self._redis.set(str(key), data)
        return str(key)
