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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Retrieves a value from a Redis data storage.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage.
        """
        return self.get(key, lambda x: int(x))
